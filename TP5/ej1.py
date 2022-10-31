def crear_numero_entero_positivo():
    while True:
        try:
            numero = float(input("Ingrese un numero:"))
            assert numero > 0, "No se permiten numeros negativos."
            assert numero % 1 == 0, "No se permiten numeros con decimales."
            break
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print("Solo se permiten numeros.")
    return int(numero)

n = crear_numero_entero_positivo()
print(n)
