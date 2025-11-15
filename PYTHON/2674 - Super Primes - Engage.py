while True:
    try:
        
        n = int(input())
        sn = str(n)
        t = '2357'
        
        
        if(n <= 1):
            print('Nada')
            continue
        elif(n <= 3):
            print('Super')
        
        elif(n%2 == 0 or n%3 == 0):
            print('Nada')
            continue
        
        else:
            primo = 1
            sprimo = 1
            
            p = 5
            
            while(p*p <= n):
                if(n%p == 0 or n%(p+2)==0):
                    primo = 0
                p+=6
            
            for i in sn:
                if( i not in t):
                    sprimo = 0
            
            if(primo == 0):
                print('Nada')
                continue
            else:
                if(sprimo == 1):
                    print('Super')
                    continue
                else:
                    print('Primo')
                    continue
            
            
            
            
    except EOFError:
        break