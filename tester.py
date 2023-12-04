from hilbertcurve.hilbertcurve import HilbertCurve
import numpy as np

class Tester:
    def __init__(self,centers,radio,maxCoord):
        self.center = centers
        self.radius = radio
        self.maxCoord = maxCoord

    def testSpecificCenter(self, pos, hilbert_curve, number_points, prints, returnValues):
        num_points = number_points

        # Generate random angles
        theta = 2.0 * np.pi * np.random.rand(num_points)  # azimuthal angle
        phi = np.arccos(2.0 * np.random.rand(num_points) - 1.0)  # polar angle

        # Convert spherical coordinates to Cartesian coordinates
        x = self.center[pos][0] + (self.radius * np.sin(phi) * np.cos(theta))
        y = self.center[pos][1] + (self.radius * np.sin(phi) * np.sin(theta))
        z = self.center[pos][2] + (self.radius * np.cos(phi))

        x = np.clip(x, 0, self.maxCoord)
        y = np.clip(y, 0, self.maxCoord)
        z = np.clip(z, 0, self.maxCoord)

        # Combine x, y, z to a list of points
        points = np.vstack([x, y, z]).T

        if prints:
            # Print 3d coord of the center of the sphere and the points on the sphere
            print('The coord is: ', self.center[pos], ' and the points are: ')
            print(points)


        # Calculate the distance from the center to each point
        sum = 0
        maxH = 0
        minH = float('inf')
        for i in range(num_points):
            h = hilbert_curve.distance_from_point([points[i][0], points[i][1], points[i][2]])
            if prints:
                print('Point ', i, ' is ', np.linalg.norm(self.center[pos] - points[i]),' away from the center and the value is ', h)
            sum += h
            if h > maxH:
                maxH = h
            if h < minH:
                minH = h

        diff = maxH - minH

        if returnValues:
            return sum/num_points, maxH, minH, diff


    def testAllCenters(self, hilbert_curve, number_points, prints, returnValues):
        num_points = number_points
        result = []
    
        for i in range(len(self.center)):
            diff = self.testSpecificCenter(i, hilbert_curve, num_points, prints, returnValues)
            result.append(diff)

        return result
