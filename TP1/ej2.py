MES_MIN = 1
MES_MAX = 12
DIA_MIN = 1

def pedir_entero_positivo():
    x = int(input("ingrese un numero:"))
    while x < 0:
        print("error")
        x = int(input("ingrese un numero:"))
    return x

def crear_tres_numeros():
    numero_1 = pedir_entero_positivo()
    numero_2 = pedir_entero_positivo()
    numero_3 = pedir_entero_positivo()
    return numero_1, numero_2, numero_3

def verificar_biciesto(año):
    es_mult_cuatro = True
    es_mult_cien = True
    es_mult_cuatrocientos = True
    es_biciesto = True
    
    if año%4 != 0:
        es_mult_cuatro = False
    if año%100 != 0:
        es_mult_cien = False
    if año%400 != 0:
        es_mult_cuatrocientos = False

    if es_mult_cuatro == False:
        es_biciesto = False
    if (es_mult_cuatro == True and es_mult_cuatrocientos == False) or es_mult_cien == True:
        es_biciesto = False
        
    return es_biciesto
        
        

def verificar_fecha_valida(dia,mes,año):
    es_fecha = True
    es_biciesto = False
    if mes == 2:
        es_biciesto = verificar_biciesto(año)
    if mes > MES_MAX or mes < MES_MIN:
        es_fecha = False
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 31 or dia < DIA_MIN:
            es_fecha = False
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30 or dia < DIA_MIN:
            es_fecha = False
    if mes == 2:
        if es_biciesto:
            if dia > 29 or dia < DIA_MIN:
                es_fecha = False
        else:
            if dia > 28 or dia < DIA_MIN:
                es_fecha = False

    return es_fecha

def mostrar_verificacion(x):
    if x:
        print("Es fecha.")
    else:
        print("No es fecha.")

dia,mes,año = crear_tres_numeros()
es_fecha = verificar_fecha_valida(dia,mes,año)
mostrar_verificacion(es_fecha)


