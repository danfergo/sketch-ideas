from keras.applications.vgg16 import VGG16
import tensorflow as tf
from keras.models import Model
from keras.layers import Conv2DTranspose, BatchNormalization, Activation, UpSampling2D
from keras.utils import print_summary

import numpy as np

class NextInstant:

    def __init__(self):
        self.build()

    def build(self):
        vgg16 = VGG16(weights='imagenet', include_top=False)

        input = vgg16.input

        conv2d_transpose = Conv2DTranspose(512, (3, 3), strides=(1, 1))(vgg16.output)
        batch_norm = BatchNormalization()(conv2d_transpose)
        act = Activation('relu')(batch_norm)

        conv2d_transpose = Conv2DTranspose(512, (3, 3), strides=(1, 1))(act)
        batch_norm = BatchNormalization()(conv2d_transpose)
        act = Activation('softmax')(batch_norm)

        up_sampling = UpSampling2D((3, 3))(act)

        conv2d_transpose = Conv2DTranspose(256, (4, 4), strides=(1, 1))(up_sampling)
        batch_norm = BatchNormalization()(conv2d_transpose)
        act = Activation('relu')(batch_norm)

        conv2d_transpose = Conv2DTranspose(128, (3, 3), strides=(2, 2))(act)
        batch_norm = BatchNormalization()(conv2d_transpose)
        act = Activation('relu')(batch_norm)

        up_sampling = UpSampling2D((3, 3))(act)

        conv2d_transpose = Conv2DTranspose(64, (4, 4), strides=(1, 1))(up_sampling)
        batch_norm = BatchNormalization()(conv2d_transpose)
        act = Activation('relu')(batch_norm)

        conv2d_transpose = Conv2DTranspose(3, (3, 3), strides=(1, 1))(act)
        batch_norm = BatchNormalization()(conv2d_transpose)
        act = Activation('relu')(batch_norm)

        output = act

        # , padding = 'valid', output_padding = None, data_format = None,
        # dilation_rate = (1, 1), activation = None, use_bias = True, kernel_initializer = 'glorot_uniform',
        # bias_initializer = 'zeros', kernel_regularizer = None, bias_regularizer = None,
        # activity_regularizer = None, kernel_constraint = None, bias_constraint = None

        self.model = Model(inputs=input, outputs=output)
        print_summary(self.model)

        self.graph = tf.get_default_graph()

        self.model.compile(optimizer='adadelta',
                           loss='mean_absolute_error')

    def train(self, images):
        with self.graph.as_default():
            self.model.fit(images[0:-1], images[1:])

        # print(np.shape(images[0:-1]))
        # print(np.shape(images[1:]))

    def predict(self, x):
        with self.graph.as_default():
            return self.model.predict(x)
