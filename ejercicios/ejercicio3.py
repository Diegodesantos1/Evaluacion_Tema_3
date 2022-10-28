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
