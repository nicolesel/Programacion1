import random

def diferenciarNaranjas(cantTotal):
    """Se simula el peso de las naranjas, y dependiendo del peso de cada una, se guarda en caja o para jugo."""
    cant_jugo=cant_cajon=peso_total_final=0
    for i in range (cantTotal):
        pesoRandom = random.randint (150,350)
        if 200<=pesoRandom<=300:
            cant_cajon += 1
            peso_total_final += pesoRandom
        else:
            cant_jugo += 1
    return cant_cajon,cant_jugo,peso_total_final

def llenarCaja(cantCajonTotal):
    """Se busca la cantidad de cajones llenos y cuantas naranjas se guardan para el proximo tramo"""
    llenos=cantCajonTotal//100
    sobrantes=cantCajonTotal%100
    return llenos,sobrantes

def llenarCamiones(pesoTotal):
    """Se identifica cuantos camiones saldran a partir del peso total"""
    return(pesoTotal//500),(pesoTotal%500)

naranjas = int (input("Ingrese la cantidad de naranjas cosechadas: "))
nar_jugo=0
nar_cajon=0
peso_total = 0

nar_jugo,nar_cajon,peso_total = diferenciarNaranjas(naranjas)

cajones_llenos,sobrante = llenarCaja(nar_cajon) 

camiones,camiones_resto = llenarCamiones(peso_total/1000)

if camiones_resto>=400:
    camiones+=1
    
print ("Cantidad de naranjas para jugo:", nar_jugo)
print ("Cantidad de naranjas para cajón:", nar_cajon)
print("Se pueden llenar",cajones_llenos, "cajones")
print ("El sobrante de naranjas que debe ser considerado para el siguiente reparto es de", sobrante, "naranjas")
print ("El peso total de las naranjas es de", peso_total, "gramos")
print("Camiones que saldran:",int(camiones))