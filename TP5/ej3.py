def buscarMes(mes):
    try:
        meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        assert 1<=mes<=12, "Numero invalido, fuera del rango"
        return meses[mes-1]
    except AssertionError as mensaje:
        print(mensaje)
        return ""


mes=int(input("Numero del mes: "))
mesNombre=buscarMes(mes)
print("el mes es: ",mesNombre.capitalize())