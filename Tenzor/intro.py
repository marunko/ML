import tensorflow as tf
import numpy as nm


x = tf.constant(4, shape=(1,1), dtype=tf.int8)
x2 = tf.constant([[1,2],
                  [6,5,]], dtype=tf.int8)
x22 = tf.constant([[1,2],
                   [6,5]], dtype=tf.int8)
x3 = tf.eye(3) # identity matrix


xx = x2 * x22 # warning it doing without rul: row *row NOT row*column
xx1 = tf.multiply(x2, x22) # warning it doing without rul: row *row NOT row*column
# use dot for right multiplication
nm.dot(x2, x22)


#==============================  INDEXING ================================================
x = tf.constant([1,2,3,4,5], dtype=tf.int8)
print(x[:])
print(x[2:])
print(x[:2])
print(x[1:4])
print(x[-2:]) # opposite to print(x[2:])
print(x[:-1],"\n")

x = tf.constant([[1,2,3],
                 [4,5,6],
                 [7,8,9]], dtype=tf.int8)
print(x[0,:])
print(x[0:2, :-1])