import csv

with open('star_naves.csv', 'r') as file:
    reader3 = csv.DictReader(file, delimiter=';')
    star_naves = list(reader3)


def ordenar_naves():
    naves = []
    for row in star_naves:
        naves.append(row['Name'])
    naves.sort()
    print(f"\n\nLas naves ordenadas por nombre son {naves}")

ordenar_naves()

def ordenar_largo():
    naves_largo = []
    for row in star_naves:
        naves_largo.append(row['Name'] + " " + row['Length'])
    naves_largo.sort() ; naves_largo.reverse()
    print(f"\n\nLas naves ordenadas por largo son {naves_largo}")

ordenar_largo()

def halcon_milenario():
    for row in star_naves:
        if row['Name'] == "Millennium Falcon":
            print(f"\n\nLa información del Millenium Falcon es {row}")

halcon_milenario()

def estrella_muerte():
    for row in star_naves:
        if row['Name'] == "Death Star":
            print(f"\n\nLa información de la Death Star es {row}")

estrella_muerte()