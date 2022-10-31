from re import L


def mostrarM(m,f,c):
    if len(m[f])==c:
        f+=1
        c=0
        print()
    if len(m)==f:
        return
    print(m[f][c],end=" ")
    return mostrarM(m,f,c+1)

m=[[2,3,6,7],[3,5],[3,3,1]]
mostrarM(m,0,0)