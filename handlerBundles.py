import numpy as np
import math
import random

from hilbertcurve.hilbertcurve import HilbertCurve

# Constants
dimensions = 3
points_per_fiber = 21


def read_bundlesdata(filename):
    A = np.fromfile(filename, dtype=np.float32)
    B = A.reshape(-1, 64)[:, 1:].reshape(-1, points_per_fiber, dimensions)
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

def createCenters(amount, data):
    ceil = maxCoord(data)
    centers = []
    for i in range(amount):
        x_float = np.float32(random.uniform(0, ceil))
        y_float = np.float32(random.uniform(0, ceil))
        z_float = np.float32(random.uniform(0, ceil))
        centers.append([x_float,y_float,z_float])

    centers = np.reshape(centers, (amount, dimensions))
    return centers