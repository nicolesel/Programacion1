def es_mayor(frase):
    return len(frase) >= numero

def filtrar_palabras(frase,numero):
    frase_partida = frase.split()
    nueva_frase = list(filter(lambda x:len(x)>=numero,frase_partida))
    nueva_frase = " ".join(nueva_frase)
    return nueva_frase

frase = input("Escriba una frase:")
numero = int(input("Caracteres minimos:"))
nueva_frase = filtrar_palabras(frase,numero)
print(nueva_frase)
