def hanoi(num, origen, destino, auxiliar):
    if num == 1:
        print(f"mover disco de {origen} a {destino}")
    else:
        hanoi(num-1, origen, auxiliar, destino)
        print(f"mover disco de {origen} a {destino}")
        hanoi(num-1, auxiliar, destino, origen)

def ejercicio1():
    hanoi(3, "origen", "destino", "auxiliar")


ejercicio1()