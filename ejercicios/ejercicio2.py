def crear_matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            matriz[i].append(0)
    return matriz

def rellenar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            matriz[i][j] = int(input(f"ingrese el numero de la posicion {i},{j}: "))
    return matriz