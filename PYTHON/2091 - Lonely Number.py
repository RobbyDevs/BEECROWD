while True:
    n = int(input())
    
    if n == 0:
        break
    
    v = sorted(list(map(int,input().split())))
    
    ant = v[0]
    c = 1
    for i in range(1,n):
        if v[i] != ant:
            
            ant = v[i]
        else:
            c+=1
        
        