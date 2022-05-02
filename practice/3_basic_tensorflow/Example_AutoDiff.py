# 자동 미분(Automatic Differentiation)
import tensorflow as tf

# y = 3x - 2 선형 관계를 갖는 데이터셋 생성
g = tf.random.Generator.from_seed(2020)
X = g.normal(shape=(10,))

Y = 3 * X - 2

print('X: ', X.numpy())
print('Y: ', Y.numpy())
