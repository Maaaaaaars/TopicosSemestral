import time
import sys
from bundleHandler import *
from tester import *
from queriesHandler import *
from plotter import *
def main():
    data = read_bundlesdata('sub7.bundlesdata')
    esferas = int(sys.argv[1])
    radio = float(sys.argv[2])
    centers = [[127,114,12],
               [127,110,31],
               [128,108,47],
               [125,105,63],
               [93,118,3],
               [94,116,3],
               [96,115,3],
               [93,115,36],
               [0,0,0],
               [0,0,0]]
    totalFibers = 10

    bitMatrix = np.zeros((totalFibers, esferas))


    start_time = time.process_time()

    for k in range(totalFibers):
        for i in range(21):
            point1 = data[k][i]
            for j in range(len(centers)):
                point2 = centers[j]
                distance = np.linalg.norm(np.array(point2) - np.array(point1))
                if distance <= radio:
                    bitMatrix[k][j] = 1


    print(data)

    end_time = time.process_time()
    print(end_time - start_time)
    #np.savetxt("exact3D.txt", bitMatrix, fmt="%d")
    print(bitMatrix)

    print('Nearest fiber from 1 is: ',nearestQeury(1, bitMatrix))
    print('Nearest fiber from 2 is: ',nearestQeury(2, bitMatrix))
    print('Nearest fiber from 4 is: ',nearestQeury(4, bitMatrix))
    print('Nearest fiber from 5 is: ',nearestQeury(5, bitMatrix))
    print('Nearest fiber from 8 is: ',nearestQeury(8, bitMatrix))

    plot_rows(data, 10)

main()
