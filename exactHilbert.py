import time
import sys
from bundleHandler import *
from tester import *
from queriesHandler import *


def main():
    data = read_bundlesdata('sub7.bundlesdata')
    esferas = int(sys.argv[1])
    radio = float(sys.argv[2])
    centers = createCenters(esferas, data)
    totalFibers = getTotalFibers(data)

    p = math.ceil(math.log(maxCoord(data), 2))
    
    hilbert_curve = HilbertCurve(p, 3)

    hilbertCenters = []
    for i in range(esferas):
        hilbertCenters.append(hilbert_curve.distance_from_point(centers[i]))

    hilbertCenters = sorted(enumerate(hilbertCenters), key=lambda x: x[1])

    bitMatrix = np.zeros((totalFibers, esferas))

    start_time = time.process_time()

    for k in range (totalFibers):
        for i in range (21):
            point1 = data[k][i]
            for j in range (len(centers)):
                point2 = hilbert_curve.point_from_distance(hilbertCenters[j][1])
                distance = np.linalg.norm(np.array(point2) - np.array(point1))
            if distance <= radio:
                bitMatrix[k][j] = 1

    end_time = time.process_time()
    print(end_time - start_time)
    #np.savetxt("exactHilbert.txt", bitMatrix, fmt="%d")
    print(bitMatrix)

main()