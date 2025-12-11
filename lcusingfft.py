import numpy as np
import matplotlib.pyplot as plt
def lcfft(x,h):
    n=len(x)
    m=len(h)
    l=n+m-1
    x1=np.fft.fft(x,l)
    x2=np.fft.fft(h,l)
    y=x1*x2
    y=np.real(np.fft.ifft(y))
    return y
x=eval(int(input('x:')))
h=eval(int(input('h:')))
result=lcfft(x,h)
print(result)
    