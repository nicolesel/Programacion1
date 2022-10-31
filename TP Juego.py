import random, sys, subprocess
from unittest.case import _AssertRaisesContext

def buscarCara(matriz,cara):
    """Busca la posicion del jugador"""
    for f in range (len(matriz)):
        for c in range (len(matriz[0])):
            if cara == matriz[f][c]:
                return f , c

def maloMov(matriz,caraMalo,caraBueno):
    
    fM,cM=buscarCara(matriz,caraMalo)
    fB,cB=buscarCara(matriz,caraBueno)
    if fB!=fM:
        if fB>fM:
            mov="S"
        else:
            mov="W"
    else:
        if cM>cB:
            mov="A"
        else:
            mov="D"
    
    return mov
    
def mover(matriz,lado,cara,vacio):
    """Mueve la posicion de :) segun el movimiento del jugador y la posicion de :( en sentido contrario"""
    f,c=buscarCara(matriz,cara)
    try:
        assert not(f==0 and lado=="W") 
        assert not(c==0 and lado=="A") 
        if lado== "W":
            matriz[f-1][c]=cara
            matriz[f][c]=vacio
        if lado=="S":
            matriz[f+1][c]=cara
            matriz[f][c]=vacio
        if lado=="A":
            matriz[f][c-1]=cara
            matriz[f][c]=vacio
        if lado=="D":
            matriz[f][c+1]=cara
            matriz[f][c]=vacio
        return True
    except IndexError:
            print("Error, no se puede la opcion",lado.upper())
            return False
    except AssertionError:
            print("Error, no se puede la opcion",lado.upper())
            return False

def creacionParedes(matriz,bloque):
    queF= [random.randint(1,23) for i in range (13)]
    queC= [random.randint(0,25) for i in range (13)]
    
    for f in range (len(matriz)):
        if f in queF:
            pos=random.randint(0,25)
            for i in range(random.randint(3,8)):
                if f!=0 and pos<25:
                    matriz[f][pos]= bloque
                    pos+=1
    for c in range (len(matriz)):
        if c in queC:
            pos=random.randint(1,23)
            for i in range(random.randint(3,8)):
                if 0<=pos<=23:
                    matriz[pos][c]= bloque
                    pos+=1
    return matriz
  
def imprimir (matriz):
    subprocess.run("clear",shell=True)
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range (filas):
        for c in range (columnas):
            print("%2s"%matriz[f][c], end="")
        print()
    
#Programa Principal

# Inicio y explicacion del juego
print("**ATRÁPAME**".center(50))        
print("\nEl jugador debe moverse por el tablero para llegar a la sailida (E) sin que :( lo atrape. Cuando el jugador o :( llegan a alguna posicion en la que se encuentra una escalera, automaticamente el personaje sube o baja. Cuando :( llega a un pozo, aparecera en otro pozo elegido al azar.\nCONTROLES:\nW = Arriba\nS = Abajo\nA = Izquierda\nD = Derecha\n")

#Creacion de la matriz (tablero del juego) y su diseño 
tamaño = 25
bueno = "\U0001F920"
malo = "\U0001F479"
salida = "\U0001F6AA"
bloque = "\U0001F6A7"
vacio="\U0001F4A0"
tablero = [[vacio]*tamaño for i in range(tamaño)]
pos_exit = random.randint(0,tamaño-1)
pos_mala = random.randint(0,tamaño-1)
pos_bueno = random.randint(0,tamaño-1)
while pos_exit == pos_mala:
    pos_exit = random.randint(0,tamaño-1)
tablero[0][pos_mala] = malo
tablero[tamaño-1][pos_bueno] = bueno
tablero[0][pos_exit] = salida
tablero=creacionParedes(tablero,bloque)
imprimir(tablero)
print()

#Se pide al jugador que elija el movimiento
movimientos = ["W","S","A","D"]
while(tablero[0][pos_exit]==salida):
    mov = input("Movimiento: ")
    mov = mov.upper()
    while mov not in movimientos:
        print ("Movimiento Invalido, ingreselo nuevamente")
        mov=input("Movimiento: ")
        mov = mov.upper()
    verif=mover(tablero,mov,bueno,vacio)
    if verif== False:
        continue
   
    else:
        imprimir(tablero)
        f,c=buscarCara(tablero,bueno)
        if f==0 and c==pos_exit:
            texto="<<<< ¡¡Ganaste!! >>>>"
            print(texto.center(70))
            break

    # Jugada del malo 
    mov=maloMov(tablero,malo,bueno)
    verif=mover(tablero,mov,malo,vacio)
    imprimir(tablero)

    """
    if mov == movimientos[0]:
        mover_arriba(tablero,mov)
    elif mov == movimientos [1]:
        mover_abajo(tablero)
    elif mov == movimientos [2]:
        mover_izquierda(tablero)
    else:
        mover_derecha(tablero)
    """



    """
    elif verif==1:
        print("Perdiste una vida")
        vidas-=1
    """
