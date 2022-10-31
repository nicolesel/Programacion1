import random

n=int(input("Ingrese N: "))
m=[]
print(m)
lista=[random.randint(0,9) for i in range(n**2)]
print(lista)
random.shuffle(lista)
print (lista)
i=0
for f in range (n):
    m.append(lista[f*n:(f+1)*n])
print(m)
