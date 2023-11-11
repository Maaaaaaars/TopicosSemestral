from bundleHandler import *
import math

class Space:
    def __init__(self, x, y, z, D, r):
        self.x = x
        self.y = y
        self.z = z
        self.D = D
        self.r = r
    
    def get_coord(self, coord_type):
        if coord_type == 'x':
            return self.x
        elif coord_type == 'y':
            return self.y
        elif coord_type == 'z':
            return self.z


def main():
    data = read_bundlesdata('sub7.bundlesdata')

    space = Space(*maxValues(data), 10, 10)

    print(space.get_coord('x'))
   


main()


    

