
def verificar(mail):
    mail=list(mail)
    error=[]
    flag=True
    if "@" in mail:
        print("ok1")
        if mail.count("@")>1:
            error.append("Hay mas de un \"@\" en el mail.\n")
            print("no ok1a")
            flag=False
            return flag, " ".join(error)

        if ("".join(mail[:mail.index("@")])).isalnum() == False:
            error.append("El usuario no es alfanumerico.\n")
            flag=False
            return flag , " ".join(error)
    else: 
        error.append("No hay \"@\" en el mail.\n")
        flag=False
        print("no ok1b")
        return flag , " ".join(error)
   
    if mail[-7:]!= list(".com.ar"):
        error.append("El final no es correcto.\n")
        flag=False 
        return flag , " ".join(error)

    else:
        if len(mail[mail.index("@")+1 : len(mail)-7])==0:
            error.append("El dominio es inexistente.\n")
            flag=False 
            return flag , " ".join(error)

        
    return flag, " ".join(error)

#Programa Principal
print("Ingrese mail, sino pulse enter y se temrinara el programa!")
mails=[]
mail="mail"
while mail!="":
    mail=input("Ingrese mail: ")
    if mail=="":
        continue
    verif,error=verificar(mail.lower())

    if verif==False:
        print("\t**Errores**\n",error)
    else:
        if mail[mail.index("@")+1:-7] not in mails:
            mails.append(mail[mail.index("@")+1:-7])

if mails==[]:
    print("No hay mails")
else:
    mails.sort()
    print("\t*MAILS*\n","\n".join(mails))
    
