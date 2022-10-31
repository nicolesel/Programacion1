def encontrarmayor (x,y,z):
    """Encuentra el mayor entre 3 números."""
    if y < x > z:
        mayor=x
    elif x < y > z:
        mayor=y
    elif x < z > y:
        mayor = z
    else:
        mayor = -1
    return  mayor

#Programa principal
num1 = float(input("Ingrese el primer número positivo: "))
num2 = float(input("Ingrese el segundo número positivo: "))
num3 = float(input("Ingrese uel tercer número positivo: "))
num_mayor = encontrarmayor (num1, num2, num3)
if num_mayor == -1:
    print ("No hay un mayor estricto")
else:
    print ("El mayor número es", num_mayor)