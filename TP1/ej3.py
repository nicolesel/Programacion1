def gastosubte(y,x):
    '''Toma el valor de la tarifa y la cantidad de viajes. Asi calcula
    el total gastado'''
    total = 0
    if 0<x<=20:
        total = x*y
    elif 20<x<=30:
        total = (20*y) + (x - 20) * tarifa * 0.8
    elif 30<x<=40:
        total = (30*y) + (x - 30) * 0.7 * y
    elif 40<x:
        total = (40*y) + (x - 40) * y * 0.6
    return total
viajes = int(input("Ingrese el numero de viajes: "))
tarifa = int(input("Ingrese el valor actual del boleto de subterraneo: "))
print(gastosubte(tarifa,viajes))