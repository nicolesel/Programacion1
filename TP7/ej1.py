digitos=0
num=int(input("Ingrese numero: "))
def buscarDigitos(num,digitos):
    if num!=0:
        digitos+=1
        return buscarDigitos(num//10,digitos)
    return digitos
digitos=buscarDigitos(num,digitos)
print("cantidad de digitos: ",digitos)