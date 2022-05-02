import tensorflow as tf
import math

# 시그모이드 함수
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

hello = tf.constant("안녕, Tensorflow")
print(hello)

rand = tf.random.uniform([1], 0, 1)
print(rand)

print(tf.executing_eagerly())

a = 1
b = 2
c = tf.math.add(a, b)
print(c)

