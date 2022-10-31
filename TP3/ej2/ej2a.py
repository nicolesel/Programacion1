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

def rellenar(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if(f==c):
                mat[f][c]= random.randint(1,10)
    return mat
n=int(input("ingrese la cantidad filas y columnas: "))
m=[[0 for i in range (n)]for i in range (n)]
imprimir(m)
m=rellenar(m)
imprimir(m)
#crearMatriz()