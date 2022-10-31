
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
    num=len(mat)+1
    for f in range(len(mat)):
        num-=1
        for c in range(len(mat[f])):
            if(c<=f):
                mat[f][c]= num
                
    return mat

    
    
n=int(input("ingrese la cantidad filas y columnas: "))
m=[[0 for i in range (n)]for i in range (n)]
imprimir(m)
m=rellenar(m)
imprimir(m)

