#Programa principal
#int("ingrese frase: ")



frase="hola como  estas   ahre"
frase=sorted(frase.split())
print(*frase)

""" o asi

def ordenar_cadena(cad):

    partida = cad.split()
    print(type(partida))
    partida.sort()
    partida=" ".join(partida)
    return partida
    

cadena = input("Ingrese una frase:")
ordenada = ordenar_cadena(cadena)
print(ordenada)


"""