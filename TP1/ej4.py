

from asyncio.base_futures import _FINISHED


def debe (plata,dio):
    """Devuelve el vuelto"""
    billeteQuinientos=0
    billetesCien=0
    billetesCincuenta=0
    billetesVeinte=0
    billetesDiez=0
    billetesCinco=0
    billetesUno=0

    cambio=dio-plata

    if cambio//500:
        billeteQuinientos=cambio//500
        cambio=cambio%500
    if cambio//100:
        billetesCien=cambio//100
        cambio=cambio%100
    if cambio//50:
        billetesCincuenta=cambio//50
        cambio=cambio%50
    if cambio//20:
        billetesVeinte=cambio//20
        cambio=cambio%20
    if cambio//10:
        billetesDiez=cambio//10
        cambio=cambio%10
    if cambio//5:
        billetesCinco=cambio//5
        cambio=cambio%5
    if cambio//1:
        billetesUno=cambio//1
        cambio=cambio%1
    return billeteQuinientos,billetesCien,billetesCincuenta,billetesVeinte,billetesDiez,billetesCinco,billetesUno
    
#Programa Principal
monto = int(input("Ingrese monto: "))
dinero=int(input("Ingrese dinero recibido: "))
if monto>dinero:
    print("error")
    quit()
b500,b100,b50,b20,b10,b5,b1=debe(monto,dinero)
print("Vuelto: ",b500," billetes de $500, ",b100," billetes de $100, ",b50," billetes de $50, ",b20," billetes de $20,  ",b10," billetes de $10,  ",b5," billetes de $5, y ",b1," billetes de $1")