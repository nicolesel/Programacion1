
import random
#def imprimir(mat):
#    for f in mat:
#        for c in f:
#           print("%3d"%c,end="")
#        print()
#   print()

def imprimir(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print("%3d"%mat[f][c],end="")
        print()
    print()

def rellenar(matriz):
    matriz =[]
    lista =list(range(1,n+1))
    lista_2 = lista[::]
    matriz.append(lista)
    for i in range (n-1):
        elemento = [lista_2.pop(n-1)]
        elemento = elemento + lista_2
        lista_2 = elemento
        lista = lista_2[:]
        matriz.append(lista)
    return matriz

    
    
n=int(input("ingrese la cantidad filas y columnas: "))
m=[[0 for i in range (n)]for i in range (n)]
imprimir(m)
m=rellenar(m)
imprimir(m)

