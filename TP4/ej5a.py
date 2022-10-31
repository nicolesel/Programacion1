def filtrar_palabras(frase,numero):
    frase_partida = frase.split()
    nueva_frase = ""
    for i in range(len(frase_partida)):
        if len(frase_partida[i]) >= numero:
            nueva_frase = nueva_frase + frase_partida[i] + " "
    return nueva_frase

frase = input("Escriba una frase: ")
numero = int(input("Caracteres minimos: "))
nueva_frase = filtrar_palabras(frase,numero)
print(nueva_frase)
