from bundleHandler import *
import math
import random

class Space:
    def __init__(self, x, y, z, D, r):
        self.x = x
        self.y = y
        self.z = z
        self.D = D
        self.r = r

        self.centers = []
        for i in range(D):
            x_float = np.float32(random.uniform(0, x))
            y_float = np.float32(random.uniform(0, y))
            z_float = np.float32(random.uniform(0, z))
            self.centers.append([x_float,y_float,z_float])
        
        self.centers = np.reshape(self.centers, (self.D, 3))

    def getCoord(self, coord_type):
        if coord_type == 'x':
            return self.x
        elif coord_type == 'y':
            return self.y
        elif coord_type == 'z':
            return self.z
        
    def getCenters(self):
        return self.centers





    

