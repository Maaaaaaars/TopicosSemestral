class Sketch():
    def __innit__(self, x, y, z, D, r):
        self.x = x
        self.y = y
        self.z = z
        self.D = D
        self.r = r







def main():
    # Create a 3D space with dimensions 10x10x10
    X_Max = 10
    Y_Max = 10
    Z_Max = 10

    space = [[[0 for z in range(X_Max)] for y in range(Y_Max)] for x in range(Z_Max)]
    
    # Print the space
    for x in range(10):
        for y in range(10):
            for z in range(10):
                print(space[x][y][z], end=' ')
            print()
        print()
