def pedir_pos(frase):
    pos = int(input("Donde termina la cadena que quiere eliminar:"))
    while pos < 0 or pos >= len(frase):
        print("Error")
        pos = int(input("Donde empieza la cadena que quiere extraer:"))
    return pos

def pedir_cant(frase,pos):
    cant = int(input("Cuantos caracteres quiere extraer:"))
    while cant < 0 or cant > (len(frase)-pos):
        print("Error")
        cant = int(input("Donde empieza la cadena que quiere extraer:"))
    return cant
    
def extraer_string(frase,inicio,cant):
    nueva_frase=""
    for i in range (len(frase)):
        if i<inicio or i>=inicio+cant:
            nueva_frase+= frase[i]
        else:
            i+=cant
    
    return nueva_frase

#Programa Principal
frase = input("Introdusca una frase:")
pos = pedir_pos(frase)
cantidad = pedir_cant(frase,pos)
extracto = extraer_string(frase,pos,cantidad)
print(extracto)
