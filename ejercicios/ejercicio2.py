
def sarrus(matriz):
    if len(matriz) == 3:
        solucion =((matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1]) - (matriz[0][2] * matriz[1][1] * matriz[2][0]) - (matriz[0][0] * matriz[1][2] * matriz[2][1]) - (matriz[0][1] * matriz[1][0] * matriz[2][2]))
        print(f"la solucion es {solucion}")
    else:
        print("La matriz no es cuadrada de 3 x 3.")


sarrus([[1, 20, 3], [4, 50, 6], [7, 80, 9]])