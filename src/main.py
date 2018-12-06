import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from math import pi
import os

from entities.robot import Robot
from entities.world import World
from agent import Agent
import threading


import time, threading

StartTime=time.time()

class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()

def loop(screen, space):
    clock = pygame.time.Clock()

    draw_options = pymunk.pygame_util.DrawOptions(screen)

    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        yield 'BEFORE_DRAW', i
        i += 1

        space.debug_draw(draw_options)

        yield 'AFTER_DRAW', i

        space.step(1 / 60.0)

        pygame.display.flip()
        clock.tick(60)


def grab_screen(screen, position, size):
    img = pygame.Surface(size)
    img.blit(screen, (0, 0), (position, size))
    numpy_img = pygame.surfarray.array3d(img)
    numpy_img = numpy_img.swapaxes(0, 1)
    return numpy_img


def main():
    x = 1600
    y = 45
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

    pygame.init()
    pygame.display.set_caption("A quick robot simulation")

    screen = pygame.display.set_mode((224, 224))

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    agent = Agent()

    robot = Robot((100, 100))
    world = World()

    space.add(*robot.build())
    space.add(*world.build())

    t = setInterval(0.1, lambda: agent.heartbit())

    try:
        for event, i in loop(screen, space):
            if event == 'BEFORE_DRAW':
                screen.fill((255, 255, 255))
            else:
                agent.on_vision(grab_screen(screen, (0, 0), (224, 224)))
    except:
        agent.die()
        t.cancel()
        # sys.exit()


if __name__ == '__main__':
    main()
