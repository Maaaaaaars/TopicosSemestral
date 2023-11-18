import time
from space import *
from hilbertcurve.hilbertcurve import HilbertCurve



def main():
    data = read_bundlesdata('sub7.bundlesdata')
    space = Space(*maxValues(data), 10, 50)
    centers = space.getCenters()
    totalFibers = getTotalFibers(data)


    p = math.ceil(math.log(maxCoord(data), 2))
    print(centers)

    print(type(centers[0][0]))


    
    hilbert_curve = HilbertCurve(p, 3)
    distances = hilbert_curve.distance_from_point(centers[0])
    print(distances)
    



        

    



main()