import tensorflow as tf
import numpy as nm
from tensorflow import keras
from keras import layers
from keras.datasets import cifar10
from keras.datasets import mnist
import os

os.environ['TFF_CPP_MIN_LOG_LEVEL'] = '2'

#Data
(x_train, y_train), (x_test, y_test)= cifar10.load_data()
x_train = x_train.astype("float32")/255.0
x_test = x_test.astype("float32")/255.0

# Layers
mod = keras.Sequential([
    keras.Input(shape=(32,32,3)),
    layers.Conv2D(32,(3,3), padding='valid', activation='relu'),
    layers.MaxPool2D(pool_size=(2,2)),
    layers.Dense(512, activation='relu'),
    layers.Dense(10,activation='softmax')
])
mod.build()

mod.summary()
