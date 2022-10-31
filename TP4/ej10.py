def filtrar_palabras(frase,palabra,cambio):
    contador = 0
    nueva_frase = frase.split()
    if palabra in nueva_frase:
        for i in range(len(nueva_frase)):
            if nueva_frase[i] == palabra:
                nueva_frase[i] = cambio
                contador += 1
    nueva_frase = " ".join(nueva_frase)
    return nueva_frase, contador

""" o """

""" esta mal! porque replace tambien cambia cuando hay una similitud dentro de la palabra: 


Escriba una frase:la venta del inventario fue inventada ayer
Que palabra de la frase quiere eliminar:venta
Por que palabra la quiere cambiar:compra
la compra del incomprario fue incomprada ayer

def filtro(frase,palabra,cambio):
    

    if palabra in frase:
        frase= frase.replace(palabra,cambio)

    contador = (frase.split()).count(cambio)

    return frase, contador
"""
frase = input("Escriba una frase:")
palabra_cambiar = input("Que palabra de la frase quiere eliminar:")
cambio = input("Por que palabra la quiere cambiar:")
nueva_frase, cont = filtrar_palabras(frase,palabra_cambiar,cambio)
print(nueva_frase)
print(cont)
