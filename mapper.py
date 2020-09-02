import numpy as np

def mapp(h):
    h=h.reshape((4,2))
    hnew=np.zeros((4,2),dtype = np.float32)

    add=h.sum(axis=1)
    hnew[0]=h[np.argmin(add)]
    hnew[3]=h[np.argmax(add)] #put 3 NOT 2

    diff=np.diff(h,axis = 1)
    hnew[1]=h[np.argmin(diff)]
    hnew[2]=h[np.argmax(diff)] #put 2 NOT 3

    return hnew
