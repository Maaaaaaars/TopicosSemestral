import time

from handlerBundles import *
from handlerQueries import *

def exact3D(dataName, maxFibers, esferas, radio):
    data = read_bundlesdata(dataName) # Obtener los datos de los bundles en un formato util
    esferas = esferas # Cantidad de esferas a usar
    radio = radio # Radio de las esferas
    centers = createCenters(esferas, data) # Crear los centros de las esferas al azar
    totalFibers = maxFibers # Obtener la cantidad maxima de fibras a procesar

    bitMatrix = np.zeros((totalFibers, esferas), dtype=np.int8) # Crear la matriz de bits

    start_time = time.process_time()
    for k in range(totalFibers): # Para cada fibra
        for i in range(points_per_fiber): # Para cada punto de la fibra
            point1 = data[k][i] # Obtener el punto
            distances = np.linalg.norm(np.array(centers) - np.array(point1), axis=1) # Calcular la distancia entre el punto y cada centro de esfera
            within_range = distances <= radio # Obtener los centros de esfera que estan dentro del radio
            bitMatrix[k][within_range] = 1 # Se marcan los bits correspondientes a la fibra y los centros de esfera dentro del radio
    end_time = time.process_time()
    print('Tiempo exact3D con ' + str(esferas) + ' esferas de radio ' + str(radio) + ': ' + str(end_time - start_time))
    
    nombre = "exact3D" + '-' + str(esferas) + '-' + str(radio) + ".txt"
    np.savetxt(nombre, bitMatrix, fmt="%d")

    return bitMatrix
