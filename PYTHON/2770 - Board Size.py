while True:
    
    try:    
        x,y,m = map(int,input().split())
        a = x*y
        for i in range(m):
            xi,yi = map(int,input().split())
            
            if xi*yi > a:
                print('Nao')
            
            else:
                print('Sim')
            
    except EOFError:
        break