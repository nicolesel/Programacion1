def a(m,n):
    while m > 0:
        if n==0:
            n=1
        else:
            n=a(m,n-1)
        m-=1
    n+=1
