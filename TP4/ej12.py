def crear_baraja():
    baraja = []
    palos = ["Oros","Bastos","Espadas","Copas"]
    for palospos in range(len(palos)):
        for i in range(12):
            baraja += [str(i+1) +" "+ palos[palospos]]
    return baraja

bar = crear_baraja()
print(bar)
