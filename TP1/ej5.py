
def funcionUno (cant):
    for i in range (cant):
        print("**********")
def funcionDos (cant):
    col=0
    for i in range (cant):
        col+=1
        for i in range (col):
             print("*",end="")
        print("")

filas=int(input("Ingrese cantidad de filas: "))
print()
funcionUno(filas)
print()
funcionDos(filas)
