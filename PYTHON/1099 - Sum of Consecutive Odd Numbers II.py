for w in range(int(input())):
    
    x,y = map(int,input().split())
    
    x,y = min(x,y),max(x,y)
    
    nn = (y-x-1)
    n = nn//2
    
    if n <0:
        print(0)
        continue
    
    if nn %2 !=0 and (x+1) %2 !=0:
        n+=1
        
    if (x+1) %2 !=0:
        x+=1
    else:x+=2
    
    if (y-1) %2 !=0: y-=1
    else: y-=2
    
    print(((x+y)*n)//2)