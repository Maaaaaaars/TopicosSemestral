import time

from handlerBundles import *
from handlerQueries import *


def exactHilbert(dataName, maxFibers, esferas, radio):
    data = read_bundlesdata(dataName) # Obtener los datos de los bundles en un formato util
    esferas = esferas # Cantidad de esferas a usar
    radio = radio # Radio de las esferas
    centers = createCenters(esferas, data) # Crear los centros de las esferas al azar
    totalFibers = maxFibers # Obtener la cantidad maxima de fibras a procesar

    p = math.ceil(math.log(maxCoord(data), 2)) # Calcular el p asociado a la curva de hilbert
    
    hilbert_curve = HilbertCurve(p, 3) # Crear la curva de hilbert

    hilbertCenters = [] # Lista de los centros de las esferas en la curva de hilbert
    for i in range(esferas):
        hilbertCenters.append(hilbert_curve.distance_from_point(centers[i])) # Calcular la distancia de cada centro a la curva de hilbert

    hilbertCenters = sorted(enumerate(hilbertCenters), key=lambda x: x[1]) # Ordenar los centros de las esferas en la curva de hilbert

    bitMatrix = np.zeros((totalFibers, esferas)) # Crear la matriz de bits

    start_time = time.process_time()
    for k in range (totalFibers): # Para cada fibra
        for i in range (points_per_fiber): # Para cada punto de la fibra
            point1 = data[k][i] # Obtener el punto
            for j in range (len(centers)): # Para cada centro de esfera
                point2 = hilbert_curve.point_from_distance(hilbertCenters[j][1]) # Obtener el centro de esfera de la curva de hilbert
                distance = np.linalg.norm(np.array(point2) - np.array(point1)) # Calcular la distancia entre el centro de esfera y el punto
            if distance <= radio: # Si la distancia es menor o igual al radio, el punto pertenece a la esfera
                bitMatrix[k][j] = 1 # Se marca el bit correspondiente a la fibra y el centro de esfera
    end_time = time.process_time()
    print('Tiempo exactHilbert con ' + str(esferas) + ' esferas de radio ' + str(radio) + ': ' + str(end_time - start_time))

    nombre = "exactHilbert" + '-' + str(esferas) + '-' + str(radio) + ".txt"
    np.savetxt(nombre, bitMatrix, fmt="%d")

    return bitMatrix

