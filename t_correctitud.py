import time
import sys
from handlerBundles import *
from tester import *
from handlerQueries import *
from t_plotter import *
def main():
    data = read_bundlesdata('sub7.bundlesdata')
    esferas = int(sys.argv[1])
    radio = float(sys.argv[2])
    centers = createCenters(esferas, data)
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


    end_time = time.process_time()
    '''
    print(end_time - start_time)
    #np.savetxt("exact3D.txt", bitMatrix, fmt="%d")
    

    print('Nearest fiber from 1 is: ',nearestQeury(1, bitMatrix))
    print('Nearest fiber from 2 is: ',nearestQeury(2, bitMatrix))
    print('Nearest fiber from 4 is: ',nearestQeury(4, bitMatrix))
    print('Nearest fiber from 5 is: ',nearestQeury(5, bitMatrix))
    print('Nearest fiber from 8 is: ',nearestQeury(8, bitMatrix))
    '''

    bitMatrix2 = np.zeros((totalFibers, esferas))
    for k in range(totalFibers):
        for i in range(21):
            point1 = data[k][i]
            distances = np.linalg.norm(np.array(centers) - np.array(point1), axis=1)
            within_range = distances <= radio
            bitMatrix2[k][within_range] = 1

    if np.array_equal(bitMatrix, bitMatrix2):
        print('Son iguales')
    
main()
