for w in range(int(input())):
    
    a,b = map(int,input().split())
    
    
    raf = ((3*a)**2)+b**2
    
    bet = (2*(a**2)) + ((5*b)**2)

    car = (-100*a)+(b**3)
    

    maior = max(raf,bet,car)
    
    if maior == raf:
        print("Rafael ganhou")
    elif maior == bet:
        print("Beto ganhou")
    else:print("Carlos ganhou")
    
