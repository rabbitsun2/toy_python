from keras.models import load_model
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import tensorflow as tf

# seed값 설정
seed = 0
np.random.seed(seed)
tf.random.set_seed(3)

# 데이터 입력
file_path = "./dataset/sonar.csv"
df = pd.read_csv(file_path, header=None)

dataset = df.values
X = dataset[:, 0:60].astype(float)
Y_obj = dataset[:, 60]

# 문자열 변환
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
#Y_encoded = tf.keras.utils.to_categorical(Y)

# 학습셋과 테스트셋의 구분
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
    test_size=0.22, random_state=seed)

# 모델 설정
model = Sequential()
model.add(Dense(24, input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='mean_squared_error', 
            optimizer='adam',
            metrics=['accuracy'])

# 모델 실행
model.fit(X_train, Y_train, epochs=130, batch_size=5)

# 모델 저장
model.save('my_model.h5')

del model # 메모리 내의 모델 삭제

# 모델 불러오기
model = load_model('my_model.h5')

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))