from bundleHandler import *

def nearestQeury(fiber, bitMatrix):
    origin = bitMatrix[fiber]
    minNorm = float('inf')
    nearest = 0
    for i in range(len(bitMatrix)):
        if i != fiber:
            binary_diff = np.abs(origin - bitMatrix[i])
            norm = np.linalg.norm(binary_diff)
            if norm < minNorm:
                minNorm = norm
                nearest = i
    return nearest

def twoCenters(center1, center2, bitMatrix):
    fibers = []
    for i in range(len(bitMatrix)):
        if bitMatrix[i][center1] == 1 and bitMatrix[i][center2] == 1:
            fibers.append(i)

    return fibers