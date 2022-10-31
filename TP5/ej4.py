
for i in range(1000000):
    try: 
        print(i+1,end=" ")
    except KeyboardInterrupt:
        resp=input("\nDesea terminar?(S/N): ")
        if resp.upper()=="S":
            break


