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
        exact = exact3D(data, maxFibers, 14000, radio)

        for j in range(4):
            ranges = rangesHilbert(data, maxFibers, esferas, radio, iterations, iterationPoints)
            av_precision = 0
            av_recall = 0

            randomFibers = random.sample(range(0, maxFibers), 25)

            for fiber in randomFibers:
                verdad = sameSignature(fiber, exact)
                estimador = sameSignature(fiber, ranges)
                verdad = set(verdad)
                estimador = set(estimador) 
                intersection = verdad & estimador
                truePositives = len(intersection)
                falsePositives = len(estimador) - truePositives
                falseNegatives = len(verdad) - truePositives
                precision = 0
                recall = 0
                if (truePositives + falsePositives != 0): precision = truePositives / (truePositives + falsePositives)
                if (truePositives + falseNegatives != 0): recall = truePositives / (truePositives + falseNegatives)
                av_precision = av_precision + precision
                av_recall = av_recall + recall
                print('Fibra: ', fiber, ' Precision: ', precision, ' Recall: ', recall)
            print('Average Precision: ', av_precision / 25, ' Average Recall: ', av_recall / 25)
            print('')
        print('-----------------------')
        maxFibers = maxFibers + 100000

main()