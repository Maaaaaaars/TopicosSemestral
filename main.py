import sys

from im_rangesHilbert import *
from im_exact3D import *


def main():
    random.seed(100)

    data = 'sub7.bundlesdata'
    maxFibers = 100000
    esferas = int(sys.argv[1])
    radio = float(sys.argv[2])
    iterations = int(sys.argv[3])
    iterationPoints = int(sys.argv[4])

    for i in range(4):
        print('Iteration: ', i)
        print('-----------------------')
        for j in range(4):
            exact = exact3D(data, maxFibers, esferas, radio)
            ranges = rangesHilbert(data, maxFibers, esferas, radio, iterations, iterationPoints)

            randomFibers = random.sample(range(0, maxFibers), 10)

            for fiber in randomFibers:
                verdad = set(sameSignature(exact[fiber], exact))
                estimador = set(sameSignature(ranges[fiber], ranges))
                intersection = verdad & estimador
                truePositives = len(intersection)
                falsePositives = len(estimador) - truePositives
                falseNegatives = len(verdad) - truePositives
                precision = truePositives / (truePositives + falsePositives)
                recall = truePositives / (truePositives + falseNegatives)
                print(precision, recall)
                print('')
        print('-----------------------')
        maxFibers = maxFibers + 100000

main()