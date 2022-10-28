
def sarrus(matriz):
    if len(matriz) == 3:
        print("La solución es:")
        print(matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1] - matriz[0][2] * matriz[1][1] * matriz[2][0] - matriz[0][1] * matriz[1][0] * matriz[2][2] - matriz[0][0] * matriz[1][2] * matriz[2][1])
    else:
        print("La matriz no es cuadrada de 3 x 3.")


sarrus([[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])

