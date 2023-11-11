import numpy as np

#Notas: El primer iterador va hasta  B-1
#El segundo iterador va hasta 21
#El tercer iterador va hasta 3

def read_bundlesdata(filename):
    A = np.fromfile(filename, dtype=np.float32)
    B = A.reshape(-1, 64)[:, 1:].reshape(-1, 21, 3)
    return B






