import tensorflow as tf
import numpy as nm
from tensorflow import keras
from keras import layers
from keras.datasets import cifar10
from keras.datasets import mnist
import os

os.environ['TFF_CPP_MIN_LOG_LEVEL'] = '2'

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train[0])
x_train = x_train.astype("float32")/255.0
x_test = x_test.astype("float32")/255.0
print("========================================================")
print(x_train[0])
print(len(x_train))
print(len(x_train[0]))
