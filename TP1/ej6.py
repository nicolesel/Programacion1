

def concatenar_numeros (x,y):
    """Concatena dos numeros enteros"""
    cantDeCeros = 0
    copia = y
    while copia != 0:
        copia = copia // 10
        cantDeCeros += 1
    aMultiplicar = 10**cantDeCeros
    numFinal = x * aMultiplicar
    numFinal += y
    return numFinal

#Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input ("Ingrese el segundo número: "))
num_final = concatenar_numeros(num1,num2)
print ("Su numero final es: ",num_final)
