while True:
    try:
        
        n,c,k = map(int,input().split())
        if n == 0 and c == 0 and k == 0:
            break
        
        v = []
        vf = [0]*k
        vr = []
        
        for i in range(n):
            v.append(list(map(int,input().split())))
            
        for i in range(len(v)):
            for j in range(len(v[i])):
                vf[v[i][j]-1] +=1
        
        men = min(vf)
        
        for i in range(len(vf)):
            if vf[i] == men:
                vr.append(i+1)
        #print(vf)
                
                        
        print(*vr,sep=' ')
        
        
    except EOFError:
        break