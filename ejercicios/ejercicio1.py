def hanoi(num, origen, destino, auxiliar):
    if num == 1:
        print(f"mover disco de {origen} a {destino}")
    else:
        hanoi(num-1, origen, auxiliar, destino)
        print(f"mover disco de {origen} a {destino}")
        hanoi(num-1, auxiliar, destino, origen)

def ejercicio1():
    numero =int(input("ingrese el numero de discos:"))
    if numero > 10:
        numero = int(input("ingrese el número de discos"))
    else:
        hanoi(numero, "origen", "destino", "auxiliar")

ejercicio1()