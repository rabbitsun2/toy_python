import tensorflow as tf

# 텐서 정의
tensor1 = tf.constant([[0, 1, 2],
                        [3, 4, 5]])

print(tensor1)

tensor_var1 = tf.Variable(tensor1)
print(tensor_var1)

print("이름: ", tensor_var1.name)
print("크기: ", tensor_var1.shape)
print("자료형: ", tensor_var1.dtype)
print("배열: ", tensor_var1.numpy())

# 변수 값 할당하기
tensor_var1.assign([[1, 1, 1],
                    [2, 2, 2]])

print(tensor_var1)

# 텐서플로 / 변수 to 텐서 변환(값 변경 불가)
tensor2 = tf.convert_to_tensor(tensor_var1)
print(tensor2)

# 텐서플로 / 변수 name 속성 변경하기
tensor_var2 = tf.Variable(tensor2, name='New Name')
print(tensor_var2.name)

tensor_var1 + tensor_var2