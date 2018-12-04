import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util


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

        yield i
        i += 1
        # ticks_to_next_ball -= 1
        # if ticks_to_next_ball <= 0:
        #     ticks_to_next_ball = 25
        #     ball_shape = add_ball(space)
        #     balls.append(ball_shape)

        #

        # balls_to_remove = []
        # for ball in balls:
        #     if ball.body.position.y < 150:
        #         balls_to_remove.append(ball)
        #
        # for ball in balls_to_remove:
        #     space.remove(ball, ball.body)
        #     balls.remove(ball)

        space.debug_draw(draw_options)

        space.step(1 / 50.0)

        pygame.display.flip()
        clock.tick(50)


def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)

    rotation_limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_limit_body.position = (200, 300)

    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (10, 10)
    l1 = pymunk.Segment(body, (0, 0), (580, 0), 5.0)
    # l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 5.0)

    # rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0,0), (0,0))
    # joint_limit = 25
    # rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100,0), (0,0), 0, joint_limit)
    #
    space.add(l1, body)
    # return l1,l2


def add_robot(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)

    # rotation_limit_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    # rotation_limit_body.position = (200, 300)

    body = pymunk.Body()
    body.position = (300, 300)
    l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 5.0)
    l2.density = 1

    rotation_center_joint = pymunk.RatchetJoint(rotation_center_body, body, 0, 10)
    # joint_limit = 25
    # rotation_limit_joint = pymunk.RatchetJoint(body, rotation_limit_body, (-100,0), (0,0), 0, joint_limit)
    #
    space.add(l2, rotation_center_joint, body)
    # return l1,l2


def add_ball(space):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(120, 380)
    body.position = x, 550
    shape = pymunk.Circle(body, radius, (0, 0))
    space.add(body, shape)
    return shape


def main():
    pygame.init()
    pygame.display.set_caption("A quick robot simulation")

    screen = pygame.display.set_mode((600, 600))

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    for i in loop(screen, space):
        screen.fill((255, 255, 255))
        if i == 0:
            # add_ball(space)
            add_L(space)
            add_robot(space)

        # print('fps')


if __name__ == '__main__':
    main()
