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

    hilbertCenters = [] # Lista de los centros de las esferas en la curva de hilbert
    for i in range(esferas):
        hilbertCenters.append(hilbert_curve.distance_from_point(centers[i])) # Calcular la distancia de cada centro a la curva de hilbert

    hilbertCenters = sorted(enumerate(hilbertCenters), key=lambda x: x[1]) # Ordenar los centros de las esferas en la curva de hilbert

    bitMatrix = np.zeros((totalFibers, esferas), dtype=int) # Crear la matriz de bits

    tester = Tester(centers, radio, maxCoord(data)) # Crear el tester

    ranges = [] # Lista de los rangos de cada centro de esfera
    for i in range(esferas): # Para cada centro de esfera
        average = 0 # Promedio de las distancias de los puntos al centro de esfera
        for j in range(iterations): # Para cada iteracion
            average += tester.testSpecificCenter(i, hilbert_curve, iterationPoints, False, True)[3] 
        
        average = average / iterations # Se calcula el promedio de las distancias de los puntos al centro de esfera
        ranges.append(average) # Se agrega el promedio a la lista de rangos


    start_time = time.process_time()
    for k in range (totalFibers): # Para cada fibra
        for i in range (points_per_fiber):
            hilberted = hilbert_curve.distance_from_point(data[k][i]) # Calcular la distancia del punto a la curva de hilbert
            for j in range (len(centers)): # Para cada centro de esfera
                if(abs(hilbertCenters[j][1] - hilberted) <= ranges[j]): # Si la distancia entre el centro de esfera y el punto es menor o igual al rango del centro de esfera
                    cFromHilbert = hilbert_curve.point_from_distance(hilbertCenters[j][1]) # Obtener el centro de esfera de la curva de hilbert
                    distance = np.linalg.norm(np.array(cFromHilbert) - np.array(data[k][i])) # Calcular la distancia entre el centro de esfera y el punto
                    if distance <= radio: # Si la distancia es menor o igual al radio, el punto pertenece a la esfera
                        bitMatrix[k][j] = 1 # Se marca el bit correspondiente a la fibra y el centro de esfera
    end_time = time.process_time()
    print('Tiempo rangesHilbert con ' + str(esferas) + ' esferas de radio ' + str(radio) + ': ' + str(end_time - start_time))    
    
    nombre = "rangesHilbert" + '-' + str(esferas) + '-' + str(radio)+ ".txt"    
    np.savetxt(nombre, bitMatrix, fmt="%d")

    return bitMatrix
    