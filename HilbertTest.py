import time
from bundleHandler import *
from tester import *

def nearestQeury(fiber, bitVector):
    origin = bitVector[fiber]
    minNorm = float('inf')
    nearest = 0
    for i in bitVector.shape[1]:
        if i != fiber:
            binary_diff = np.abs(origin - bitVector[i])
            norm = np.linalg.norm(binary_diff)
            if norm < minNorm:
                minNorm = norm
                nearest = i
    return nearest



def main():
    data = read_bundlesdata('sub7.bundlesdata')
    radio = 20
    esferas = 100
    centers = createCenters(esferas, data)
    totalFibers = 10

    p = math.ceil(math.log(maxCoord(data), 2))
    
    hilbert_curve = HilbertCurve(p, 3)

    hilbertCenters = []
    for i in range(esferas):
        hilbertCenters.append(hilbert_curve.distance_from_point(centers[i]))

    hilbertCenters = sorted(enumerate(hilbertCenters), key=lambda x: x[1])

    matrix = np.zeros((totalFibers, esferas))

    start_time = time.process_time()
    for k in range (totalFibers):
        for i in range (21):
            hilberted = hilbert_curve.distance_from_point(data[k][i])
            low = 0
            high = esferas - 1
            last = None
            while low <= high:
                mid = (low + high) // 2
                last = mid
                if hilbertCenters[mid][1] < hilberted:
                    low = mid + 1
                elif hilbertCenters[mid][1] > hilberted:
                    high = mid - 1
                elif hilbertCenters[mid][1] == hilberted:
                    break
            
            cFromHilbert = hilbert_curve.point_from_distance(hilbertCenters[last][1])
            distance = np.linalg.norm(np.array(cFromHilbert) - np.array(data[k][i]))
            if distance <= radio:
                matrix[k][hilbertCenters[last][0]] = 1
    end_time = time.process_time()
    print(end_time - start_time)
    print(matrix.shape)
    


            
    
    


    
main()