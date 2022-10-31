def esgapful(n):
    ultimacifra = n%10
    primeracifra = n
    while primeracifra>10:
        primeracifra//=10
    divisor = primeracifra*10+ultimacifra
    return n%divisor==0

# Programa principal
limite = int(input("Límite superior? "))
print(f"Los números gapful menores que {limite} son:")
for i in range(100, limite+1):
    if esgapful(i):
        print(i, end=" ")