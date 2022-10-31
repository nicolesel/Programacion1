import random


num=random.randint(1,501)
print(num)
adivina=0
cont=0
while num!=adivina:
    try: 
        adivina=int(input("Ingrese: "))
        if num==adivina:
            break
        assert adivina>num, "El numero es menor"
        assert adivina<num, "El numero es mayor"
        
    except AssertionError as men:
        cont+=1
        print(men)
    except ValueError:
        cont+=1
        print("Error de valor")
   
    finally:
        
        print("intentos: ",cont)


print("MUY BIEN, cant de intentos: ",cont)