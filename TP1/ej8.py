from operator import truediv


def imprimir_dias():
    print("Do Lu Mi Ma Ju Vi Sa")
    print("--------------------")

def verificar_biciesto(año):
    es_mult_cuatro=True
    es_mult_cien=True
    es_mult_cuatrocientos=True
    es_biciesto=True
    if año%4!=0:
        es_mult_cuatro=False
    if año%100 !=0:
        es_mult_cien=False
    if año%400 !=0:
        es_mult_cuatrocientos=False

    if es_mult_cuatro==False:
        es_biciesto=False
    if es_mult_cuatro==True and es_mult_cuatrocientos==False and es_mult_cien==True:
        es_biciesto=False
    return es_biciesto

def verificar_cant_dias(mes,año):
    dia_mes=0
    es_biciesto=verificar_biciesto(año)
    if mes in [1,3,5,7,8,10,12]:
        dia_mes=31
    if mes in [4,6,9,11]:
        dia_mes=30
    if mes==2:
        if es_biciesto:
            dia_mes=29
        else:
            dia_mes=28
    return dia_mes

def diadelasemana(dia,mes,año):
    if mes <3:
        mes=mes+10
        año-=1
    else:
        mes-=2
    siglo=año//100
    año2=año%100
    diasem=(((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem<0:
        diasem=diasem+7
    return diasem

def imprimir_dias_mes(mes,año):
    imprimir_dias()
    posicion_inicial=diadelasemana(1,mes,año)
    contador=1
    pos=posicion_inicial
    while posicion_inicial>0:
        print("    ",end="")
        posicion_inicial-=1
    dias=verificar_cant_dias(mes,año)
    while contador<=dias:
        if pos==7:
            print()
            pos=0
        else:
            print("%2d"%contador,end="  ")
            contador+=1
            pos+=1
    print("")

mes=int(input("Mes: "))
año=int(input("Año: "))
imprimir_dias_mes(mes,año)