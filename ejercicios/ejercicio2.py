
def sarrus(matriz):
    if len(matriz) == 3:
        print("La solución es:")
        print(matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1] - matriz[0][2] * matriz[1][1] * matriz[2][0] - matriz[0][1] * matriz[1][0] * matriz[2][2] - matriz[0][0] * matriz[1][2] * matriz[2][1])
    else:
        print("La matriz no es cuadrada de 3 x 3.")

def sarrus_iterativo(matriz):
    if len(matriz) == 3:
        determinante = 0
        for i in range(3):
            determinante += matriz[0][i] * matriz[1][(i + 1) % 3] * matriz[2][(i + 2) % 3] - matriz[0][i] * matriz[1][(i + 2) % 3] * matriz[2][(i + 1) % 3]
        print(f"La solución es {determinante}")
    else:
        print("La matriz no es cuadrada de 3 x 3.")

def ejercicio2():
    sarrus([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])

    sarrus_iterativo([[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])

