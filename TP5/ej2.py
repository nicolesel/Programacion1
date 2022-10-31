def suma (n1,n2):
    try:
        n1=float(n1)
        n2=float(n2)
        suma=n1+n2
    except ValueError:
        print("Error en el valor")
        return -1
    return suma






n1=input("Ingrese numero: ")
n2=input("Ingrese numero: ")
print(suma(n1,n2))