import numpy as np
import matplotlib.pyplot as plt

data = [[2, 81], [4, 93], [6, 91], [8, 97]]

# x = 공부시간
# y = 점수
x = [i[0] for i in data]
y = [i[1] for i in data]

# 그래프 나타내기
plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

# 넘파이 배열
x_data = np.array(x)
y_data = np.array(y)

print("x data의 값={}".format(x_data))
print("y data의 값={}".format(y_data))

# 기울기a와 절편b의 값 초기화
a = 0 
b = 0

# 학습률
lr = 0.02

# 반복횟수
epochs = 2001

for i in range(epochs):
    y_pred = a * x_data + b
    error = y_data - y_pred

    a_diff = -(2/len(x_data)) * sum(x_data * (error))    
    b_diff = -(2/len(x_data)) * sum(error)

    a = a - lr * a_diff
    b = b - lr * b_diff

    if i % 100 == 0:
        print("epoch=%.f, 기울기=%.004f, 절편=%.004f" % (i, a, b))


y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()