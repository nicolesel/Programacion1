import random

def imprimirmatriz(mat):
    for fila in mat:
        for elem in fila:
            print("%3d" %elem, end="")
        print()

def minimosporcolumna(mat):
    filas = len(mat)
    columnas = len(mat[0])
    sumacolumnas = [0] * columnas
    for c in range(columnas):
        for f in range(filas):
            sumacolumnas[c]+=mat[f][c]
    return sumacolumnas

# Programa principal
filas = int(input("Cantidad de filas? "))
columnas = int(input("Cantidad de columnas? "))
matriz = []
for f in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(random.randint(0,9))
imprimirmatriz(matriz)
sumacolumnas = minimosporcolumna(matriz)
for i in range(columnas):
    print("---", end="")
print()
minimo = min(sumacolumnas)
listaminimos = []
for i, suma in enumerate(sumacolumnas):
    print("%3d" %suma, end="")
    if suma==minimo:
        listaminimos.append(i)
print()
print()
print("El mínimo por columna es", minimo, "y se encontró en las columnas", end=" ")
print(*listaminimos, sep=", ")