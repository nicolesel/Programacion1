def espandigital(num):
    lista = [0] * 10
    while num!=0:
        digito = num % 10
        num = num // 10
        lista[digito] = 1
    return True if sum(lista)==10 else False

n = int(input("Ingrese un número entero: "))
if espandigital(n):
    print(n, "es pandigital")
else:
    print(n, "no es pandigital")