import time
from space import *
from tester import *



def main():
    data = read_bundlesdata('sub7.bundlesdata')
    space = Space(*maxValues(data), 10, 50)
    centers = space.getCenters()
    totalFibers = getTotalFibers(data)


    p = math.ceil(math.log(maxCoord(data), 2))
    
    hilbert_curve = HilbertCurve(p, 3)
    tester = Tester(centers, 10)

    tester.testAllCenters(hilbert_curve, 100, False, False)


    
main()