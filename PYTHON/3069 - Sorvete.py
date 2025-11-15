caso = 0
while True:
    caso+=1
    
    p,s = map(int,input().split())
    
    if s+p == 0:
        break
    v = []
    for i in range(s):
        a,b = map(int,input().split())
        v.append([a,b])
        
    v.sort()
    #print(v)
    print("Teste",caso)
    
    if (s==1): print(a,b)
    
    else:
        va = []
        e = v[0][0]
        d = v[0][1]

        for i in range(1,s):
            if v[i][0] - d >= 1:
                va.append([e,d])
                e = v[i][0]
                d = v[i][1]
                
            else:
                if d < v[i][1]:
                    d = v[i][1]
        va.append([e,d])
        for i in va:
            print(*i,sep=' ')
    print()
                
        
    
    
    