from cProfile import label
from pickletools import optimize
from statistics import mode
from sklearn import metrics
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 셈플 데이터셋 생성
x = np.arange(1, 6)
y = 3 * x + 2

print(x)
print(y)

# 1. 입력 데이터 형태
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=[4]),
    tf.keras.layers.Dense(5),
    tf.keras.layers.Dense(1)
])

# 모델 요약
model.summary()

# 2. 단순선형회귀 모델 정의
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])    
])

# 모델 요약
model.summary()

# 8. 컴파일
# 긴 문자열 지정
model.compile(optimizer='sgd', loss='mean_squared_error',
            metrics=['mean_squared_error', 'mean_absolute_error'])

# 짧은 문자열 지정
model.compile(optimizer='sgd', loss='mse', metrics=['mse', 'mae'])

# 용어:
# MSE(Mean Squared Error, 평균 제곱 오차)
# SGD(Stochastic Gradient Descent, 확률적 경사 하강법)

# 9. 훈련
model.fit(x, y, epochs = 5)

# 10. 단순 선형회귀 모델 생성
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

# 컴파일
model.compile(optimizer='sgd', loss='mse', metrics=['mae'])

# 훈련
history = model.fit(x, y, epochs = 1200)

# 11. 시각화
# 20 epoch까지 Loss 수렴에 대한 시각화
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['mae'], label='mae')

plt.xlim(-1, 20)
plt.title("Loss")
plt.legend()
plt.show()

# 12. 검증
model.evaluate(x, y)

# 예측
model.predict([10])