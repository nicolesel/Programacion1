import random

def convertirRomanos (x, y):
    if x >= 1000:
        cant_m = x // 1000
        y.append ("M" * cant_m)
        x = x - (1000 * cant_m)
    if x >= 900:
        cant_cm = x // 900
        y.append ("CM" * cant_cm)
        x = x - (900 * cant_cm)   
    if x >= 500:
        cant_d = x // 500
        y.append ("D" * cant_d)
        x = x - (500 * cant_d)
    if x >= 400:
        cant_cd = x // 400
        y.append ("CD" * cant_cd)
        x = x - (400 * cant_cd)
    if x >= 100:
        cant_c = x // 100
        y.append ("C" * cant_c)
        x = x - (100 * cant_c)
    if x >= 90:
        cant_xc = x // 90
        y.append ("XC" * cant_xc)
        x = x - (90 * cant_xc)
    if x >= 50:
        cant_l = x // 50
        y.append ("L" * cant_l)
        x = x - (50 * cant_l)
    if x >= 40:
        cant_xl = x // 40
        y.append ("XL" * cant_xl)
        x = x - (100 * cant_xl)
    if x >= 10:
        cant_x = x // 10
        y.append ("X" * cant_x)
        x = x - (10 * cant_x)
    if x >= 9:
        cant_ix = x // 9
        y.append ("IX" * cant_ix)
        x = x - (9 * cant_ix)
    if x >= 5:
        cant_v = x // 5
        y.append ("V" * cant_v)
        x = x - (5 * cant_v)
    if x >= 4:
        cant_iv = x // 4
        y.append ("IV" * cant_iv)
        x = x - (4 * cant_iv)
    if (x >= 1) and (x > 0):
        cant_i = x // 1
        y.append ("I" * cant_i)
        x = x - (1 * cant_i)
    return "".join(y)

#Programa principal

numero = random.randint (0,3999)
    
romanos = []
numeros_en_romanos = convertirRomanos (numero, romanos)
print ("El", numero, "en numeros romanos es: ", numeros_en_romanos)
