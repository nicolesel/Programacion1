def diasiguiente(dia, mes, año):
    """ Devuelve el día siguiente a la fecha recibida como parámetro """
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        cantdias = 31
    elif mes in [4, 6, 9, 11]:
        cantdias = 30
    elif mes == 2:
        if (año%4 == 0 and año%100 != 0) or año%400==0:
            cantdias = 29
        else:
            cantdias = 28
    else:
        cantdias = -1
    dia = dia + 1
    if dia>cantdias:
        dia = 1
        mes = mes + 1
        if mes>12:
            mes = 1
            año = año + 1
    return dia, mes, año

def sumardias(dia, mes, año, n):
    """ Suma N días a una fecha y devuelve tres enteros con la nueva fecha """
    for i in range(n):
        dia, mes, año = diasiguiente(dia, mes, año)
    return dia, mes, año

def fecha2int(dia, mes, año):
    """ Recibe una fecha y devuelve un entero concatenando el año, el mes y el día """
    return año*10000 + mes*100 + dia

def calculardiasentrefechas(d1, m1, a1, d2, m2, a2):
    """ Calcula cuántos días hay entre dos fechas recibidas como parámetros
        y devuelve un entero con dicha cantidad """
    # Primero nos aseguramos que la fecha1 sea menor que la fecha2. Si no, las intercambiamos
    # Concatenamos la fecha en formato AAMMDD para compararlas directamente
    fecha1 = fecha2int(d1, m1, a1)
    fecha2 = fecha2int(d2, m2, a2)
    if fecha1>fecha2:
        aux = d1
        d1 = d2
        d2 = aux
        aux = m1
        m1 = m2
        m2 = aux
        aux = a1
        a1 = a2
        a2 = aux
    # Ahora que sabemos que la fecha1 es menor o igual que la fecha2, comenzamos a contar los días que las separan
    n = 0
    while fecha2int(d1, m1, a1)!=fecha2int(d2, m2, a2):  # Mientras las fechas sean distintas...
        d1, m1, a1 = diasiguiente(d1, m1, a1)            # ...le sumamos un día a la fecha menor
        n = n + 1                                        # y contamos el día sumado
    return n

# Programa principal
print("Ingrese una fecha:")
d = int(input("Día? "))
m = int(input("Mes? "))
a = int(input("Año? "))
print()
dias = int(input("Cuántos días desea sumarle? "))
d, m, a = sumardias(d, m, a, dias)
print("La nueva fecha es %d/%d/%d" %(d, m, a))
print()
print("Ingrese los datos de la fecha 1:")
d1 = int(input("Día? "))
m1 = int(input("Mes? "))
a1 = int(input("Año? "))
print()
print("Ingrese los datos de la fecha 2:")
d2 = int(input("Día? "))
m2 = int(input("Mes? "))
a2 = int(input("Año? "))
print()
dias = calculardiasentrefechas(d1, m1, a1, d2, m2, a2)
print("Hay", dias, "dias entre ambas fechas")