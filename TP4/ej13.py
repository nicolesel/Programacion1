def calcular_digitos(n):
    digitos = 0
    auxi = n
    while auxi > 0:
        digitos += 1
        auxi = auxi//10
    return digitos

def poner_1_dig(cad,n):
    nueva = cad[:]
    if n == 1:
        nueva += "uno" + " "
    elif n == 2:
        nueva += "dos" + " "
    elif n == 3:
        nueva += "tres" + " "
    elif n == 4:
        nueva += "cuatro" + " "
    elif n == 5:
        nueva += "cinco" + " "
    elif n == 6:
        nueva += "seis" + " "
    elif n == 7:
        nueva += "siete" + " "
    elif n == 8:
        nueva += "ocho" + " "
    elif n == 9:
        nueva += "nueve" + " "
    return nueva

def poner_2_dig(cad,n):
    nueva = cad[:]
    auxi = n
    if n >= 10 and n < 16:
        if n == 10:
            nueva += "diez" + " "
        elif n == 11:
            nueva += "once" + " "
        elif n == 12:
            nueva += "doce" + " "
        elif n == 13:
            nueva += "trece" + " "
        elif n == 14:
            nueva += "catorce" + " "
        elif n == 15:
            nueva += "quince" + " "
            
    elif auxi == 20:
        nueva += "veinte" + " "
    elif auxi == 30:
        nueva += "treinta" + " "
    elif auxi == 40:
        nueva += "cuarenta" + " "
    elif auxi == 50:
        nueva += "cincunta" + " "
    elif auxi == 60:
        nueva += "sesenta" + " "
    elif auxi == 70:
        nueva += "setenta" + " "
    elif auxi == 80:
        nueva += "ochenta" + " "
    elif auxi == 90:
        nueva += "noventa" + " "
    else:
        auxi = (n//10) * 10
        if auxi == 10:
            nueva += "dieci"
        elif auxi == 20:
            nueva += "veinti"
        elif auxi == 30:
            nueva += "treinta y "
        elif auxi == 40:
            nueva += "cuarenta y "
        elif auxi == 50:
            nueva += "cincunta y "
        elif auxi == 60:
            nueva += "sesenta y "
        elif auxi == 70:
            nueva += "setenta y "
        elif auxi == 80:
            nueva += "ochenta y "
        elif auxi == 90:
            nueva += "noventa y "
        auxi = n   
        auxi = auxi%10
        nueva = poner_1_dig(nueva,auxi)
    
    return nueva

def poner_3_dig(cad,n):
    nueva = cad[:]
    auxi = n
    if n == 100:
        nueva = "cien "
    else:
        auxi = (n//100) * 100
        if auxi == 100:
            nueva += "ciento "
        elif auxi == 200:
            nueva += "doscientos "
        elif auxi == 300:
            nueva += "trescientos "
        elif auxi == 400:
            nueva += "cuatrocientos "
        elif auxi == 500:
            nueva += "quinientos "
        elif auxi == 600:
            nueva += "seiscientos "
        elif auxi == 700:
            nueva += "setecientos "
        elif auxi == 800:
            nueva += "ochocientos "
        elif auxi == 900:
            nueva += "novecientos "
        auxi = n   
        if auxi%100 != 0:
            auxi = auxi%100
            nueva = poner_2_dig(nueva,auxi)

    return nueva

def cambiar_numero_string(n):
    num_letras = ""
    digitos = 0
    if n < 0:
        n = n *-1
        num_letras += "menos "
        
    if n != 0:
        digitos = calcular_digitos(n)
    auxi = n
        
    if n == 0:
        num_letras += "cero"

    if digitos > 9 and digitos < 13:
        auxi = n//(1000000000)
        if digitos == 10:
            if auxi != 1:
                num_letras = poner_1_dig(num_letras,auxi)
        elif digitos == 11:
            num_letras = poner_2_dig(num_letras,auxi)
        elif digitos == 12:
            num_letras = poner_3_dig(num_letras,auxi)
        if "uno" in num_letras:
           num_letras = num_letras.replace("uno","un")
        num_letras += "mil "
        auxi = n%(1000000000)
        n = auxi
        if n < 1000000:
            num_letras += "millones "
            auxi = n%(1000000)
            n = n%(1000000)
        digitos = calcular_digitos(auxi)
        
    if digitos > 6 and digitos < 10:
        auxi = n//(1000000)
        if digitos == 7:
            num_letras = poner_1_dig(num_letras,auxi)
        elif digitos == 8:
            num_letras = poner_2_dig(num_letras,auxi)
        elif digitos == 9:
            num_letras = poner_3_dig(num_letras,auxi)
        
        if num_letras == "uno ":
            num_letras = num_letras.replace("uno","un millon")
        else:
            if "uno" in num_letras:
                num_letras = num_letras.replace("uno","un")
            num_letras += "millones "
        auxi = n%(1000000)
        n = n%(1000000)
        digitos = calcular_digitos(auxi)
        
    if digitos > 3 and digitos < 7:
        auxi = n//(1000)
        if digitos == 4:
            if auxi != 1:
                num_letras = poner_1_dig(num_letras,auxi)
        elif digitos == 5:
            num_letras = poner_2_dig(num_letras,auxi)
        elif digitos == 6:
            num_letras = poner_3_dig(num_letras,auxi)
        if "uno" in num_letras:
           num_letras = num_letras.replace("uno","un")
        num_letras += "mil "
        auxi = n%(1000)
        digitos = calcular_digitos(auxi)
                
    if digitos == 3:
        num_letras = poner_3_dig(num_letras,auxi)
    elif digitos == 2:
        num_letras = poner_2_dig(num_letras,auxi)
    elif digitos == 1 and n != 0:
        num_letras = poner_1_dig(num_letras,auxi)
        
    num_letras = num_letras.capitalize()
    return num_letras

numero = int(input("Ingrese un numero:"))
cad = cambiar_numero_string(numero)
print(cad)
