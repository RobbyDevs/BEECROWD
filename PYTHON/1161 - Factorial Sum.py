while True:
    
    try:
        m,n = map(int,input().split())
        
        fm = fn = 1
        
        for i in range (m, 0, -1):
            fm = fm * i
        for i in range (n, 0, -1):
            fn = fn * i
        
            
        print(fm+fn)
        
        
    except EOFError:
        break