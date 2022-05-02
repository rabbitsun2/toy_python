from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold

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

# 10개의 파일로 쪼갬
n_fold = 30

skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)

# 빈 accuracy 배열
accuracy = []

# 모델의 설정, 컴파일, 실행
for train, test in skf.split(X, Y):
    model = Sequential()
    model.add(Dense(24, input_dim=60, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # 모델 컴파일
    model.compile(loss='mean_squared_error', 
                optimizer='adam',
                metrics=['accuracy'])

    # 모델 실행
    model.fit(X[train], Y[train], epochs=100, batch_size=5)

    k_accuracy = "%.4f" % (model.evaluate(X[test], Y[test])[1])
    accuracy.append(k_accuracy)

# 결과 출력
print("\n %.f fold accuracy:" % n_fold, accuracy)

# 평균 출력
sum = 0.0
for a in accuracy:
    sum += float(a)

print(" average: %.4f" % (float(sum / n_fold)))