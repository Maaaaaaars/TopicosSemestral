import time
import sys
from bundleHandler import *
from tester import *
from queriesHandler import *


def exact3D(esferas, radio):

    '''
    esferas = int(sys.argv[1])
    radio = float(sys.argv[2])
    '''

    data = read_bundlesdata('sub7.bundlesdata')


    esferas = esferas
    radio = radio


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
    print('Tiempo exact3D con ' + esferas + 'esferas de radio ' + radio + ': ' + end_time - start_time)
    nombre = "exact3D" + '-' + str(esferas) + '-' + str(radio)+ ".txt"
    np.savetxt(nombre, bitMatrix, fmt="%d")
    
    return bitMatrix
