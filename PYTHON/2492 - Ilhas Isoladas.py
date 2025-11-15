while True:
    n = int(input())
    if n == 0:
        break


    va = []
    vb = []
    for i in range(n):
        
        a,_,b = map(str,input().split())
        
        va.append(a)
        vb.append(b)
    
    
    #isfunc
    
    if len(set(va)) < n:
        print('Not a function.')
    else:
        if len(set(vb)) < n:
            print('Not invertible.')
        else:
            print('Invertible.')
    #print('>>>>')
    
