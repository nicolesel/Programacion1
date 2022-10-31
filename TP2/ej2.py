def generadorLista (lista,numero):
    for i in range (1,numero+1) :
        lista.append(i**2)
    return lista
#Programa principal
listaOriginal=[]
n=0
while(n<=0):
    n=int(input("Ingrese un numero mayor o igual a 1: "))
listaOriginal=generadorLista(listaOriginal,n)
print(listaOriginal)