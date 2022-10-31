#Es capicua?

def esCapicua(palabra):
    inicio=0
    final=len(palabra)-1
    flag=True
    while inicio<final and flag==True:
        if palabra[inicio] == palabra[final]:
            inicio+=1
            final-=1
        else:
            flag=False
    return flag
        

#Programa Principal
string=input("Ingrese string: ")
es=esCapicua(string.lower())

if es==True:
    print("Es capicua")
else:
    print("No es capicua")
