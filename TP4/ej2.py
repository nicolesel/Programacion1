#"Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas"

cadena = input ("Ingrese una frase (hasta 80 caracteres): ")
while len(cadena)>80:
    print("Frase incorrecta")
    cadena = input ("Ingrese una frase (hasta 80 caracteres): ")


medio = (80 - len(cadena)) // 2
palabra=" "*medio + cadena + " "*medio
print (palabra,len(palabra))
print(f"{cadena:-^80}")



