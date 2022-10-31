#2.Desarrollar un programa para generar una lista por comprensión con los números entre 1 y N que sean múltiplos de 7 o que terminen con el dígito 7. El valor de N se ingresa desde el teclado. Luego se solicita ordenar la lista utilizando como criterio de ordenamiento la suma de los dígitos de cada número. Mostrar por pantalla la lista obtenida antes y después del ordenamiento. No se permite el uso de cadenas de caracteres. Ejemplo:Límite superior? 100[7, 14, 17, 21, 27, 28, 35, 37, 42, 47, 49, 56, 57, 63, 67, 70, 77, 84, 87, 91, 97, 98][21, 14, 42, 7, 70, 17, 35, 27, 63, 28, 37, 91, 47, 56, 57, 84, 49, 67, 77, 87, 97, 98]
def sumardig(num):
    suma = 0
    while num!=0:
        suma = suma + num%10
        num = num // 10
    return suma

n = int(input("Límite superior? "))
lista = [i for i in range(1, n+1) if i%10==7 or i%7==0]
print(lista)
lista.sort(key=sumardig)
print(lista)