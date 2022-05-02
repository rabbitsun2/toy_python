from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

import pandas as pd
import numpy
import tensorflow as tf
import os

#seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

#데이터입력
df_pre = pd.read_csv('./dataset/wine.csv', header=None)
df = df_pre.sample(frac=1)
dataset = df.values
X = dataset[:,0:12]
Y = dataset[:,12]

#모델설정
model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#모델컴파일
model.compile(loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

#모델 저장 폴더 설정
model_dir = './model'
if not os.path.exists(model_dir):
    os.mkdir(model_dir)

#모델 저장 조건설정
modelpath = "./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_accuracy', verbose=1, save_best_only=True)

#모델실행
model.fit(X, Y, epochs=200, batch_size=200, validation_split=0.2, verbose=0, callbacks=[checkpointer] )

#결과출력
#print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))

