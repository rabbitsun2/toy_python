import tensorflow as tf
import numpy as np

# 1차원 배열 정의
py_list = [10., 20., 30.]           # 파이썬 리스트 배열
num_arr = np.array([10., 10., 10.]) # 넘파이 배열

# 텐서 변환
vec1 = tf.constant(py_list, dtype=tf.float32)
vec2 = tf.constant(num_arr, dtype=tf.float32)

# 텐서 출력
print("vec1:", vec1)
print("vec2:", vec2)

# 랭크 확인
print(tf.rank(vec1))
print(tf.rank(vec2))

# 덧셈 함수(텐서)
add1 = tf.math.add(vec1, vec2)
print("result:", add1)
print("rank:", tf.rank(add1))

# 덧셈 연산자(파이썬 내장)
add2 = vec1 + vec2
print("result:", add2)
print("rank:", tf.rank(add2))

# tf.math 모듈 함수
print(tf.math.subtract(vec1, vec2))
print(tf.math.multiply(vec1, vec2))
print(tf.math.divide(vec1, vec2))
print(tf.math.mod(vec1, vec2))
print(tf.math.floordiv(vec1, vec2))

# 파이썬 연산자
print(vec1 - vec2)
print(vec1 * vec2)
print(vec1 / vec2)
print(vec1 % vec2)
print(vec1 // vec2)

# 합계 구하기
print(tf.reduce_sum(vec1))
print(tf.reduce_sum(vec2))

# 거듭제곱
print(tf.math.square(vec1))

# 거듭제곱(파이썬 연산자)
print(vec1 ** 2)

# 제곱근
print(tf.math.sqrt(vec2))

# 제곱근(파이썬 연산자)
print(vec2**0.5)

# 브로드캐스팅 연산
print(vec1 + 1)
