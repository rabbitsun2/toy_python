from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf
import pandas as pd

#np.random.seed(3)
#tf.random.set_seed(3)

# Numpy 
#dataset = np.loadtxt("dataset/pima-indians-diabetes.csv", delimiter=",")

df = pd.read_csv("dataset/pima-indians-diabetes.csv",
         names = ["a", "b", "c", "d", "e", "f", "g", "h", "i"])

# print(df[["a","g"]])
# print(df.describe())

# dataset = df.values

# X = dataset[:,0:8]
# Y = dataset[:,8]
X = df[["a", "b", "c", "d", "e", "f", "g", "h"]]
Y = df[["i"]]


model = Sequential()
model.add(Dense(12, input_dim = 8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])

model.fit(X, Y, epochs = 200, batch_size = 10)
#model.fit(dx, dy, epochs = 200, batch_size = 10)

print("\n Accuracy: %.4f" %(model.evaluate(X, Y)[1]))
#print("\n Accuracy: %.4f" %(model.evaluate(dx, dy)[1]))