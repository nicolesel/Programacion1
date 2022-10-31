def suma (n1,n2):
    try:
        n1=float(n1) , "numero 1"
        n2=float(n2) , "numero 1"
        suma=n1+n2
    except ValueError as mensaje:
        print("Error en el valor del numero",mensaje)
        return -1
    
    return suma






n1=input("Ingrese numero: ")
n2=input("Ingrese numero: ")
print(suma(n1,n2))