def filtrar_palabras(frase,numero):
    frase_partida = frase.split()
    
    frasesita= ([frase_partida[i] for i in range(len(frase_partida)) if len(frase_partida[i])>=numero])
    nueva_frase = " ".join(frasesita)
    return nueva_frase

frase = input("Escriba una frase:")
numero = int(input("Caracteres minimos:"))
nueva_frase = filtrar_palabras(frase,numero)
print(nueva_frase)

