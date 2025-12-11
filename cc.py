import numpy as np
def circ_conv(x,h):
    
    x=np.pad(x,(0,N-len(x)))
    h=np.pad(h,(0,N-len(h)))
    circ_mat=np.zeros((N,N))
    for i in range(N):
        circ_mat[i]=np.roll(x,i)
    mat=circ_mat.transpose() @ h
    return mat    
    

x=eval(input("Enter list 1:"))
h=eval(input("Enter list 2:"))
N=np.max([len(x),len(h)])
result=circ_conv(x,h)
print("Circular Convolution:",result)