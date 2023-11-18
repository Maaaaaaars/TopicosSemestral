from space import *


def main():
    data = read_bundlesdata('sub7.bundlesdata')

    space = Space(*maxValues(data), 10, 50)

    totalFibers = getTotalFibers(data)
    centers = space.getCenters()
    normalVector = np.zeros((totalFibers, len(centers)))
    #normalVector =  np.reshape(normalVector, (totalFibers, 10))


    for k in range (totalFibers):
        print(k)
        for i in range (21):
            point1 = data[k][i]
            for j in range (len(centers)):
                point2 = centers[j]
                distance = np.linalg.norm(np.array(point2) - np.array(point1))
                if distance <= 50:
                    normalVector[k][j] = 1
        
    print(normalVector)
        

    



main()