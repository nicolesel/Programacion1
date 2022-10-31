lista=[]
while True:
    num=int(input("Ingrese num"))
    if num!=-1:
        lista.append(num)
    else: 
        break
if lista==[]:
    print("Lista VACIA")
    
else:
    print(lista)
    errores=0
    while errores<3: 
        try:
            num=int(input("Ingrese posicion"))
            pos=lista.index(num)
            print("Numero en pos: ",pos)
            break
        except ValueError:
            errores+=1
            print("NO EXISTE EN LA LISTA")

