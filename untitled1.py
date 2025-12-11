import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
h = np.array([1,1,1,0])

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)   # added dtype=complex (important)
    for k in range(N):   
        for n in range(N):    
            ang = (-2j * k * np.pi * n / N)   
            X[k] += x[n] * np.exp(ang)
    return X

def cc(x,h):    
    N = np.max((len(x), len(h)))    
    x = np.pad(x, (0, N - len(x)))    
    h = np.pad(h, (0, N - len(h)))    
    y_mat = np.zeros([N, N])   
    
    for i in range(N):   
        # ↓↓↓ changed this line ↓↓↓
        y_mat[i] = np.roll(h, i)    # roll h instead of x to get (n - k) order
    
    return y_mat @ x    # removed transpose

lhs = dft(x * h)
X = dft(x)
H = dft(h)
rhs = (1 / len(x)) * (cc(X, H))

print(np.round(np.real(rhs)))
print(np.round(np.real(lhs)))
