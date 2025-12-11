import matplotlib.pyplot as plt
def linear_convolution(x, h):
    n = len(x)
    m = len(h)
    y = [0] * (n + m - 1)   
    for i in range(n):
        for j in range(m):
            y[i + j] += x[i] * h[j]
    return y

x = [1, 2, 3,4]
h = [4, 3, 2]
result = linear_convolution(x, h)
print(result)
plt.subplot(3,1,1)
plt.title("x")
plt.stem(x)
plt.subplot(3,1,2)
plt.title("h")
plt.stem(h)
plt.subplot(3,1,3)
plt.stem(result)
plt.title("y")
plt.tight_layout()
plt.show()