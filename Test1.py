from space import *


def main():
    data = read_bundlesdata('sub7.bundlesdata')

    space = Space(*maxValues(data), 10, 50)

    totalFibers = getTotalFibers(data)
    centers = space.getCenters()
    normalVector = np.zeros((totalFibers, len(centers)))
    #normalVector =  np.reshape(normalVector, (totalFibers, 10))

    #for i in range(totalFibers): #for each fiber
    #    for j in range(21): #for each point
    #        for k in range(len(centers)): #for each center
    #            point1 = data[i][j] #3D point
    #            point2 = centers[k] #center
    #            distance = np.linalg.norm(np.array(point2) - np.array(point1)) #distance between point and center
    #            if distance <= 10:
    #                normalVector[i][k] = 1 #if distance is less than 10, then the point is in the center

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