from email.mime import image
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
    num=1
    for f in range (len(mat)):
        for c in range (len(mat[f])):
            if f%2==0 and c%2!=0:
                mat[f][c]=num
                num+=1
            elif f%2!=0 and c%2==0:
                mat[f][c]=num
                num+=1
    return mat

    
    
    
n=int(input("ingrese la cantidad filas y columnas: "))
m=[[0 for i in range (n)]for i in range (n)]
imprimir(m)
m=rellenar(m)
imprimir(m)

