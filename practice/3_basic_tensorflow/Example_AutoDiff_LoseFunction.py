# 자동 미분(Automatic Differentiation) 
from sklearn.metrics import mean_squared_error
import tensorflow as tf

# Loss 함수 정의
def cal_mse(X, Y, a, b):
    Y_pred = a * X + b
    squared_error = (Y_pred - Y) ** 2
    # tf.reduce_mean() 함수 = 평균값 계산
    mean_squared_error = tf.reduce_mean(squared_error)
    
    return mean_squared_error

# y = 3x - 2 선형 관계를 갖는 데이터셋 생성
g = tf.random.Generator.from_seed(2020)
X = g.normal(shape=(10,))

Y = 3 * X - 2

print('X: ', X.numpy())
print('Y: ', Y.numpy())


# tf.GradientTape로 자동 미분 과정을 기록

a = tf.Variable(0.0)
b = tf.Variable(0.0)

EPOCHS = 200

for epoch in range(1, EPOCHS + 1):

    with tf.GradientTape() as tape:
        mse = cal_mse(X, Y, a, b)

    grad = tape.gradient(mse, {'a': a, 'b': b})

    d_a, d_b = grad['a'], grad['b']

    a.assign_sub(d_a * 0.05)
    b.assign_sub(d_b * 0.05)

    if epoch % 20 == 0:
        print("EPOCH %d - MSE: %.4f ---- a: %.2f ---- b: %.2f" %(epoch, mse, a, b))