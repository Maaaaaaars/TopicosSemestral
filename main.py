import sys

from im_rangesHilbert import *
from im_exact3D import *


def main():
    random.seed(100)

    data = 'sub7.bundlesdata'
    maxFibers = 500000
    esferas = int(sys.argv[1])
    radio = float(sys.argv[2])
    iterations = int(sys.argv[3])
    iterationPoints = int(sys.argv[4])

    #preciso = exact3D(data, maxFibers, esferas, radio)
    preciso = np.loadtxt("exact3D-1400-4.txt", dtype=int)
    print(preciso)
    ''''
    print("Exacto terminado")
    print("")

    ranges = rangesHilbert(data, maxFibers, esferas, radio, iterations, iterationPoints)
    print("Ranges terminado")

    randomFiber = random.randint(0, preciso.shape[0] - 1)
    print("Fibra aleatoria: " + str(randomFiber))
    print("")

    print(sameSignature(randomFiber, preciso))
    print("")
    print(sameSignature(randomFiber, ranges))
    '''

main()