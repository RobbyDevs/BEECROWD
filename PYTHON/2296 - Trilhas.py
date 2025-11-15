n = int(input())
id = []

for w in range(n):
    
    v = list(map(int,input().split()))
    
    l = v[0]
    v.pop(0)
    
    
    #print(v)
    
    subE = subD = 0
    ce = 0
    cd = 0
    for i in range(l-1):
        if v[i+1]-v[i] >= subD: #---->
            subD = v[i+1]-v[i]
        if v[i+1]-v[i] >0:
            cd+=1
        if v[i]- v[i+1] > subE:#<----
            subE = v[i]- v[i+1]
            ce +=1
        if v[i]- v[i+1] > 0:
            ce +=1
            
    a = [subE,ce]
    b = [subD,cd]
    #print(a,b)
        
    if a<b:
        id.append(a)
        #print('>>',a)
    else:
        id.append(b)
        #print('>>',b)
        
men = [100000,100000]
ind = 0
for i in range(n):
    if id[i] < men:
        men = id[i]
        ind = i
    if id[i][0] == 0:
        ind = i
        break
        
#print(id)
print(ind+1)


