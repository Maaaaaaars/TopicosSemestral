import time
import sys
from bundleHandler import *
from tester import *
from queries import *


def main(args):
    data = read_bundlesdata('sub7.bundlesdata')
    esferas = args[1]
    radio = args[2]
    centers = createCenters(esferas, data)
    totalFibers = getTotalFibers(data)

    bitMatrix = np.zeros((totalFibers, esferas))

    start_time = time.process_time()

    for k in range (totalFibers):
        for i in range (21):
            point1 = data[k][i]
            for j in range (len(centers)):
                point2 = centers[j]
                distance = np.linalg.norm(np.array(point2) - np.array(point1))
                if distance <= radio:
                    bitMatrix[k][j] = 1

    end_time = time.process_time()
    print(end_time - start_time)
    np.savetxt("exact3D.txt", bitMatrix, fmt="%d")
    print(bitMatrix)