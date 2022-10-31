# Practica 3, ejercicio 2g

n = int(input("Tamaño de la matriz? "))
# Generar matriz
mat = [ ]
for f in range(n):
    mat.append([0]*n)
# Relleno en espiral
contador = 1
for i in range(n//2+1):
    # Fila superior del rei
    for c in range(i,n-i):
        mat[i][c] = contador
        contador += 1
    # Columna derecha del rei
    for f in range(i+1,n-i):
        mat[f][n-1-i] = contador
        contador = contador + 1
    # Fila inferior del rei
    for c in range(n-2-i,i-1,-1):
        mat[n-1-i][c] = contador
        contador = contador + 1
    # Columna izquierda del rei
    for f in range(n-2-i,i,-1):
        mat[f][i] = contador
        contador = contador + 1
# Imprimir matriz
for f in range(n):
    for c in range(n):
        print("%3d" %mat[f][c], end="")
    print()
