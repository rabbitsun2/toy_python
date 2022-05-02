from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

file_path = "./dataset/iris.csv"

df = pd.read_csv(file_path, names=["sepal_length", 
        "sepal_width", "petal_length", "petal_width", "species"])

# 그래프 출력
sns.pairplot(df, hue='species')
plt.show()

# 데이터 분류
dataset = df.values
#X = dataset[:,0:4].astype(float)
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
#Y_obj = dataset[:,4]
Y_obj = df[["species"]]

# 문자열을 숫자로 변환
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
Y_encoded = tf.keras.utils.to_categorical(Y)

# 모델의 설정
model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

# 모델 컴파일
model.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])
        
# 모델 실행
model.fit(X, Y_encoded, epochs=50, batch_size=1)

# 결과 출력
print("\n Accuracy: %.4f" %(model.evaluate(X, Y_encoded)[1]))