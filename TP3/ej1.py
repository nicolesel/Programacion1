
import random
from stringprep import map_table_b2

def imprimir(mat,f,c):
    for i in range (f):
        for k in range (c):
            print("%2d"%mat[i][k],end="")
        print("")
    print()

def rellenar(mat,f,c):
    for i in range (f):
        for k in range (c):
            mat[i][k]=random.randint(0,9)
    return mat

def ascender(mat,f):
    mat2=[]
    mat2=mat.copy()
    k=0
    for i in range (f-1,-1,-1):
        mat[i]=mat2[k]
        k+=1
    return m

def cambiarFilas(matriz,fila_1,fila_2):
    aux = matriz[fila_1]
    matriz[fila_1]= matriz[fila_2]
    matriz[fila_2] = aux
    return matriz

def cambiarColumnas(matriz,col1,col2):
    for i in range (len(matriz)):
        aux = matriz[i][col1]
        matriz[i][col1] = matriz[i][col2]
        matriz[i][col2] = aux
    return matriz

#Programa principal
filas=3
columnas=3
m=[[0]*columnas for i in range (filas)]
imprimir(m,filas,columnas)
m=rellenar(m,filas,columnas)
imprimir(m,filas,columnas)
m=ascender(m,filas)
imprimir(m,filas,columnas)
fila1=int(input("Ingrese las fila 1 que sea cambiar:"))
fila2=int(input("Ingrese las fila 2 que sea cambiar:"))
imprimir(cambiarFilas(m,fila1-1,fila2-1),filas,columnas)
col1=int(input("Ingrese las columna 1 que sea cambiar:"))
col2=int(input("Ingrese las columna 2 que sea cambiar:"))
imprimir(cambiarColumnas(m,col1-1,col2-1),filas,columnas)