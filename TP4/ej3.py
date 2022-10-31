
def buscarCod(numero):
    i=0
    num1=""
    num2=""
    while i<=len(numero)-1:
        if i%2==0:
            num1+=numero[i]
        else:
            num2+=numero[i]
        i+=1
    return num1,num2
#Programa Principal
codigo=input("Ingrese codigo: ")
cod1,cod2=buscarCod(codigo)

print(f"Codigo 1: {cod1} y el Codigo 2: {cod2}")