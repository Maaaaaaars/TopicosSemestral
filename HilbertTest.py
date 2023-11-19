import time
from space import *
from hilbertcurve.hilbertcurve import HilbertCurve



def main():
    data = read_bundlesdata('sub7.bundlesdata')
    space = Space(*maxValues(data), 10, 50)
    centers = space.getCenters()
    totalFibers = getTotalFibers(data)


    p = math.ceil(math.log(maxCoord(data), 2))
    
    hilbert_curve = HilbertCurve(p, 3)
    thecenter = centers[0]

    num_points = 100
    radius = 10

    # Generate random angles
    theta = 2.0 * np.pi * np.random.rand(num_points)  # azimuthal angle
    phi = np.arccos(2.0 * np.random.rand(num_points) - 1.0)  # polar angle

    # Convert spherical coordinates to Cartesian coordinates
    x = thecenter[0] + (radius * np.sin(phi) * np.cos(theta))
    y = thecenter[1] + (radius * np.sin(phi) * np.sin(theta))
    z = thecenter[2] + (radius * np.cos(phi))

    # Combine x, y, z to a list of points
    points = np.vstack([x, y, z]).T
    print(thecenter)
    print(points)

    sum = 0
    maxH = 0
    minH = float('inf')
    for i in range(num_points):
        h = hilbert_curve.distance_from_point([points[i][0], points[i][1], points[i][2]])
        print('Point ', i, ' is ', np.linalg.norm(thecenter - points[i]),' away from the center and the value is ', h)
        sum += h
        if h > maxH:
            maxH = h
        if h < minH:
            minH = h


    print('Average distance in Hilbert space is ', sum/num_points)
    print('Max distance in Hilbert space is ', maxH)
    print('Min distance in Hilbert space is ', minH)
    print('Range is ', maxH - minH)


    
    



        

    



main()