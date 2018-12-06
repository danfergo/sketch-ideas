from viz import Viz
from models.next_instant import NextInstant
import numpy as np

class Agent:
    def __init__(self, ):
        self.viz = Viz()
        self.next_instant = NextInstant()
        self.vision_memory =  []
    def on_vision(self, image):
        self.vision_memory = ([image] + self.vision_memory)[:10]


    def heartbit(self):
        if len(self.vision_memory) == 0:
            return
        p_batch = np.expand_dims(self.vision_memory[0], axis=0)

        self.next_instant.train(np.asarray(self.vision_memory))

        # print(np.shape(p_batch))
        predicted = self.next_instant.predict(p_batch)
        # print(predicted[0])

        # print(len(self.vision_memory))

        self.viz.show('input', self.vision_memory[0])
        self.viz.show('predicted', predicted[0])





    def die(self):
        self.viz.stop()
