import time

from handlerBundles import *
from handlerQueries import *


def binaryHilbert(dataName, maxFibers, esferas, radio):
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
            hilberted = hilbert_curve.distance_from_point(data[k][i]) # Calcular la distancia del punto a la curva de hilbert
            low = 0 # Inicializar los valores para la busqueda binaria
            high = esferas - 1 
            last = None # Ultimo centro de esfera que se encontro
            while low <= high: # Busqueda binaria para encontrar el centro de esfera mas cercano
                mid = (low + high) // 2 
                last = mid 
                if hilbertCenters[mid][1] < hilberted:
                    low = mid + 1 
                elif hilbertCenters[mid][1] > hilberted:
                    high = mid - 1
                elif hilbertCenters[mid][1] == hilberted:
                    break 
            
            cFromHilbert = hilbert_curve.point_from_distance(hilbertCenters[last][1]) # Obtener el centro de esfera de la curva de hilbert
            distance = np.linalg.norm(np.array(cFromHilbert) - np.array(data[k][i])) # Calcular la distancia entre el centro de esfera y el punto
            if distance <= radio: # Si la distancia es menor o igual al radio, el punto pertenece a la esfera
                bitMatrix[k][hilbertCenters[last][0]] = 1 # Se marca el bit correspondiente a la fibra y el centro de esfera
    end_time = time.process_time()
    print('Tiempo binaryHilbert con ' + str(esferas) + ' esferas de radio ' + str(radio) + ': ' + str(end_time - start_time))

    nombre = "binaryHilbert" + '-' + str(esferas) + '-' + str(radio) + ".txt"
    np.savetxt(nombre, bitMatrix, fmt="%d")

    return bitMatrix

