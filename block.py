import numpy as np
import matplotlib.pyplot as plt
x=eval(input('x:'))
y=np.arange(1,100)
L=int(input("enter the length: "))
def lc(x,h):
    n = len(x)
    m = len(h)
    X = [0] * (n + m - 1)   
    for i in range(n):
        for j in range(m):
            X[i + j] += x[i] * h[j]
    return X
def block_conv(x,h,L):
    N=len(x)
    M=len(h)
    Y=np.zeros(N+M-1)
    i=0
    while i<N:    
        x_block=x[i:i+L]
        y_block=lc(x_block,h)
        Y[i:i+len(y_block)]+=y_block
        i+=L
    return Y
result=block_conv(x,y,L)
print(result)
plt.stem(result)
plt.show()