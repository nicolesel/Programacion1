def acotarcadena (x,y):
    subcadena = x[len(x)-y:]
    return subcadena

#Programa principal
cadena = input("Ingrese la cadena de caracteres: ")
cantidad = int(input("Ingrese la cantidad de caracteres finales: "))
cadena_final = acotarcadena (cadena,cantidad)
print (cadena_final)