from ejercicios import ejercicio1
from ejercicios import ejercicio2
from ejercicios import ejercicio3
from ejercicios import ejercicio5

def lanzador():
    eleccion = 0
    if eleccion == 1:
        ejercicio1.ejercicio1()
    elif eleccion == 2:
        ejercicio2.ejercicio2()
    elif eleccion == 3:
        ejercicio3.ejercicio3()
    elif eleccion == 5:
        ejercicio5.ejercicio5()
