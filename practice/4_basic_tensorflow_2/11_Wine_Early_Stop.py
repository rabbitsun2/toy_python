from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

import pandas as pd
import numpy as np
import tensorflow as tf
import os
import matplotlib.pyplot as plt

#seed 값 설정
seed = 3
np.random.seed(seed)
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
modelpath = "./model/{epoch:02d}-{val_accuracy:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_accuracy', verbose=1, save_best_only=True)

early_stopping_callback = EarlyStopping(monitor='val_accuracy', patience=100)

#모델실행
history = model.fit(X, Y, epochs=2000, batch_size=500,
        validation_split=0.33, callbacks=[checkpointer, early_stopping_callback] )

#결과출력
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))

# y_vloss에 테스트셋으로 실험 결과의 오차 값을 저장
y_vloss = history.history['val_loss']

# y_acc에 학습셋으로 측정한 정확도의 값을 저장
y_acc = history.history['val_accuracy']

# x값을 지정하고 정확도를 파란색으로, 오차를 빨간색으로 표시
x_len = np.arange(len(y_acc))
plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
plt.plot(x_len, y_acc, "o", c="blue", markersize=3)

plt.show()