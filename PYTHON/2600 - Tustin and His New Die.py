for w in range(int(input())):
    
    e = int(input())
    
    a,b,c,d, = map(int,input().split())
    
    f = int(input())
    
    v = [a,b,c,d,e,f]
    v.sort()
    
    
    va = [1,2,3,4,5,6]
    
    if v == va:
        
        if (a+c == 7) and (b+d == 7) and (e+f == 7):
            print('SIM')
        else:
            print('NAO')
    else:
        print('NAO')
            
