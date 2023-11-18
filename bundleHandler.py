import numpy as np
import math

#Notas: El primer iterador va hasta  B-1
#El segundo iterador va hasta 21
#El tercer iterador va hasta 3

def read_bundlesdata(filename):
    A = np.fromfile(filename, dtype=np.float32)
    B = A.reshape(-1, 64)[:, 1:].reshape(-1, 21, 3)
    return B

def maxValues(data):
    max_x = 0
    max_y = 0
    max_z = 0
    for trajectory in data:
        for coord in trajectory:
            max_x = max(max_x, coord[0])
            max_y = max(max_y, coord[1])
            max_z = max(max_z, coord[2])
    
    max_x = math.ceil(max_x / 10.0) * 10
    max_y = math.ceil(max_y / 10.0) * 10
    max_z = math.ceil(max_z / 10.0) * 10
    return max_x, max_y, max_z

def maxCoord(data):
    maxC = np.amax(data)
    maxC = math.ceil(maxC / 10.0) * 10
    return maxC

def getTotalFibers(data):
    return data.shape[0]