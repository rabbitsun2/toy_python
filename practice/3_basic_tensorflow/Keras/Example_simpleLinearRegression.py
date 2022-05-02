import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)

y = 3 * x + 2

print(x)
print(y)

# 시각화
plt.plot(x, y)
plt.title('y = 3x + 2')
plt.show()
