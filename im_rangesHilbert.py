import time

from handlerBundles import *
from handlerQueries import *
from tester import *


def rangesHilbert(dataName, maxFibers, esferas, radio, iterations, iterationPoints):
    data = read_bundlesdata(dataName) # Obtener los datos de los bundles en un formato util
    esferas = esferas # Cantidad de esferas a usar
    radio = radio # Radio de las esferas
    iterations = iterations # Cantidad de iteraciones
    iterationPoints = iterationPoints # Cantidad de puntos por iteracion
    centers = createCenters(esferas, data) # Crear los centros de las esferas al azar
    totalFibers = maxFibers # Obtener la cantidad maxima de fibras a procesar

    p = math.ceil(math.log(maxCoord(data), 2)) # Calcular el p asociado a la curva de hilbert
    
    hilbert_curve = HilbertCurve(p, 3) # Crear la curva de hilbert

    centersHilbert = [] # Lista de los centros de las esferas en la curva de hilbert
    for i in range(esferas):
        centersHilbert.append(hilbert_curve.distance_from_point(centers[i])) # Calcular la distancia de cada centro a la curva de hilbert
    centersHilbert = np.array(centersHilbert)

    tester = Tester(centers, radio, maxCoord(data)) # Crear el tester
    ranges = [] # Lista de los rangos de cada centro de esfera
    for i in range(esferas): # Para cada centro de esfera
        average = 0 # Promedio de las distancias de los puntos al centro de esfera
        for j in range(iterations): # Para cada iteracion
            average += tester.testSpecificCenter(i, hilbert_curve, iterationPoints, False, True)[3] 
        
        average = average / iterations # Se calcula el promedio de las distancias de los puntos al centro de esfera
        ranges.append(average) # Se agrega el promedio a la lista de rangos

    dataHilbert = [] # List of the points of the bundles on the Hilbert curve
    for i in range(totalFibers): # For each fiber
        fiber_data = [] # Create a new list for this fiber
        for j in range(points_per_fiber):
            fiber_data.append(hilbert_curve.distance_from_point(data[i][j])) # Calculate the distance of each point to the Hilbert curve
        dataHilbert.append(fiber_data) # Append the list of distances for this fiber to dataHilbert

    bitMatrix = np.zeros((totalFibers, esferas), dtype=np.int8) # Crear la matriz de bits

    start_time = time.process_time()
    for k in range(totalFibers): # Para cada fibra
        for i in range(points_per_fiber): # Para cada punto de la fibra
            point = dataHilbert[k][i] # Obtener el punto
            distances = centersHilbert - point # Calcular la distancia entre el punto y cada centro de esfera
            within_range = distances <= ranges # Obtener los centros de esfera que estan dentro del radio
            bitMatrix[k][within_range] = 1 # Se marcan los bits correspondientes a la fibra y los centros de esfera dentro del radio
    end_time = time.process_time()

    print('Tiempo rangesHilbert con ' + str(esferas) + ' esferas de radio ' + str(radio) + ': ' + str(end_time - start_time))    
    
    return bitMatrix
    