frase="Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no leva huesos. Sólo los espejos de azabache de sus ojos duros cual dos escarabajos de cristal negros."
frase=frase.lower()
palabra="UADE"
palabra=palabra.lower()

hay=0
k=0

for i in range(len(frase)):
    if frase[i]==palabra[k]:
        k+=1
        if k== len(palabra):
            hay+=1
            k=0

print(hay,"veces se encontro la palabra",palabra)