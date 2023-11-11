from reading import *
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
    max_x = 0
    max_y = 0
    max_z = 0
    for trajectory in data:
        for coord in trajectory:
            max_x = max(max_x, coord[0])
            max_y = max(max_y, coord[1])
            max_z = max(max_z, coord[2])

    print(f'Max X: {max_x}, Max Y: {max_y}, Max Z: {max_z}')

    ceil_x = math.ceil(max_x / 10.0) * 10
    ceil_y = math.ceil(max_y / 10.0) * 10
    ceil_z = math.ceil(max_z / 10.0) * 10

    print(f'Ceil X: {ceil_x}, Ceil Y: {ceil_y}, Ceil Z: {ceil_z}')

    space = Space(ceil_x, ceil_y, ceil_z, 10, 10)

    print(f'X: {space.get_coord("x")}, Y: {space.get_coord("y")}, Z: {space.get_coord("z")}, D: {space.D}, R: {space.r}')

main()


    

