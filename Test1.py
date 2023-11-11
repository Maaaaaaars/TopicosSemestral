from space import *


def main():
    data = read_bundlesdata('sub7.bundlesdata')

    space = Space(*maxValues(data), 10, 10)

    print(space.getCoord('x'))

    C = space.getCenters()
    print(C)


main()