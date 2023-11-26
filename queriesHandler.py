from bundleHandler import *

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