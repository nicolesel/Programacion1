from math import sqrt
from multiprocessing.sharedctypes import Value


num=input("Ingrese numero: ")
try:
    num=int(num)
    assert num>0, "El numero es negativo"
except ValueError:
    print("Ingreso un valor erroneo")
except AssertionError as mensaje:
    print(mensaje)
else:
    raiz=sqrt(num)
    print(raiz)