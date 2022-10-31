import random
from tokenize import Number

def rellenar(lista):
    """Rellenar lista"""
    cantidad=random.randint(10,99)
    for i in range (cantidad):
        lista.append(random.randint(1000,9999))
    
    return lista

def sumar(lista):
    """Devuelve la suma de la lista"""
    return sum(lista)

def eliminar(lista,value):
    """Elimina el valor ingresado de la lista"""
    if value in lista:
        cant=lista.count(value)
        print("Hay %d elementos del valor %.2f en la lista"%(cant,value))
        for i in range (cant):
                lista.remove(value)
    else:
        print("El elemento ingresado no esta en la lista.")
    return lista
def esCapicua(lista):
    es=True
    inicio=0
    final=len(lista)-1
    while inicio<final:
        if lista[inicio]!=lista[final]:
            es=False
            break
        else:
            inicio+=1
            final-=1
    return es
#Programa Principal
listaOriginal=[]
rellenar(listaOriginal)
print("Lista:",listaOriginal)
sum=sumar(listaOriginal)
print("Suma de la lista:",sum)
valor= int(input("Ingrese el valor a eliminar: "))
listaOriginal=eliminar(listaOriginal,valor)
print("Lista actualizada:",listaOriginal)
es=esCapicua([1,2,3,4,5,3,2,1])
if es==True:
    print("es capicua!")
else:
    print("No es capicua:(")
