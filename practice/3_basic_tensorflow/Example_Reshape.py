# 텐서플로 불러오기
import tensorflow as tf

# 랭크-1 텐서 정의
tensor = tf.constant(range(0, 24))
print(tensor)

tensor1 = tf.reshape(tensor, [3, 8])
print(tensor1)

# 4 by 1로 나눔(행6 x 열4)
tensor2 = tf.reshape(tensor1, [-1, 4])
print(tensor2)

# 1차원으로 변환
tensor3 = tf.reshape(tensor2, [-1])
print(tensor3)

tensor4 = tf.reshape(tensor3, [-1, 3, 4])
print(tensor4)

tensor5 = tf.reshape(tensor4, [3, 2, 4])
print(tensor5)

tensor6 = tf.reshape(tensor5, [3, 2, 2, 2])
print(tensor6)
