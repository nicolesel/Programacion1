def eliminar (lista, valor):
    if valor in lista:
        cant=0
        for i in range (0,len(lista)-cant):
            if valor == lista[i]:
                lista.remove(lista[i])
                cant+=1

lista=[1,2,3,4,2,6,7,6,8]
eliminar(lista,2)
print(lista)
eliminar(lista,7)
print(lista)
eliminar(lista,6)
print(lista)