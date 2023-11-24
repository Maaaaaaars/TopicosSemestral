import time
from bundleHandler import *
from tester import *
import bisect


def main():
    data = read_bundlesdata('sub7.bundlesdata')
    radio = 5
    esferas = 10
    centers = [[93,120,4],[93,120,4],[93,120,4],[93,120,4],[93,120,4],[93,120,4],[93,120,4],[93,120,4],[93,120,4],[93,120,4]]
    totalFibers = 1

    p = math.ceil(math.log(maxCoord(data), 2))
    
    hilbert_curve = HilbertCurve(p, 3)

    hilbertCenters = []
    for i in range(esferas):
        hilbertCenters.append(hilbert_curve.distance_from_point(centers[i]))

    hilbertCenters = sorted(enumerate(hilbertCenters), key=lambda x: x[1])

    matrix = np.zeros((totalFibers, esferas))

    print(hilbertCenters)
    

    #for k in range (totalFibers):
    #    print(data[k])

    start_time = time.process_time()
    for k in range (totalFibers):
        for i in range (21):
            #hilberted = hilbert_curve.distance_from_point(data[k][i])
            
            for j in range(esferas):
                cFromHilbert = hilbert_curve.point_from_distance(hilbertCenters[j][1])
                print(np.linalg.norm(np.array(cFromHilbert) - np.array(data[k][i])))
            #if distance <= radio:
            #    matrix[k][hilbertCenters[last][0]] = 1
    end_time = time.process_time()

    print(end_time - start_time)
    print('')
    print(matrix)
    



            
    
    


    
main()