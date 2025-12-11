import numpy as np
import matplotlib.pyplot as plt
def tlc(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1
    toeplitz_matrix = np.zeros((len_y, len_x))
    for i in range(len_y):
        for j in range(len_x):
            if 0 <= i - j < len_h:
                toeplitz_matrix[i][j] = h[i - j]
    y = toeplitz_matrix @ x
    return y

x = [1,7,8,5,3,9,0] 
h = [1,2,0,4]
y=tlc(x,h)
print(y)
plt.subplot(3,1,1)
plt.stem(x)
plt.title('x')
plt.subplot(3,1,2)
plt.stem(h)
plt.title('h')
plt.subplot(3,1,3)
plt.stem(y)
plt.title('y')

plt.show()