import numpy as np
'lc using cc'
x=eval(input('x:'))
h=eval(input('h:'))
N= len(x)+len(h)-1

def lc(x,h):
    x=np.pad(x,(0,N-len(x)))
    h=np.pad(h,(0,N-len(h)))
    mat=np.zeros((N,N))
    for i in range(N):
        mat[i]=np.roll(x,i)
        print(mat)
        
    return mat.transpose() @ h
result=lc(x,h)
print(result)
