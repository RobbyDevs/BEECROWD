for w in range(int(input())):
    t1c, op, t2v = map(str,input().split())
    t1c = int(t1c)
    t2v = int(t2v)
    
    
    t2c, op, t1v = map(str,input().split())
    t2c = int(t2c)
    t1v = int(t1v)
    
    
    t1 = t1c+t1v
    t2 = t2c+t2v
    
    if t1>t2:
        print('Time 1')
    elif t2>t1:
        print('Time 2')
        
    else:
        if t1v>t2v:
            print('Time 1')
        
        elif t2v>t1v:
            print('Time 2')
        else:
            print('Penaltis')
            
