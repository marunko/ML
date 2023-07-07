import os
import tensorflow as tf
import numpy as nm
from tensorflow import keras
from keras import layers
from keras.datasets import mnist

os.environ['TFF_CPP_MIN_LOG_LEVEL'] = '2'

#Data
(x_train, y_train), (x_test, y_test)= mnist.load_data()

x_train = x_train.reshape(-1, 28*28).astype("float32")/255.0
x_test = x_test.reshape(-1, 28*28).astype("float32")/255.0


# Layers
mod = keras.Sequential([
    keras.Input(shape=(784)),
    layers.Dense(512, activation='relu'),
    layers.Dense(10)
])

#Teaching
mod.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    metrics=["accuracy"]
)

mod.fit(x_train, y_train, batch_size=32, epochs=2, verbose=1)
mod.evaluate(x_test, y_test, verbose=1)