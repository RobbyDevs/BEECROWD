while True:
    n,m = map(int,input().split())
    if n == 0 and m ==0:
        break
    r = 0
    v = list(map(int,input().split()))
    
    ma = max(v)
    mi = min(v)
    dis = ma-mi+1
    
    vz = [0 for i in range(dis+1)]
    
    for i in v:
        vz[i-1]+=1
    
    for i in vz:
        if i >1:
            r+=1
            
    print(r)