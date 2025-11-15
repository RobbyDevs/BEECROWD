ct = int(input())
for w in range(ct):
    
    
    m,c = map(int,input().split())
    v = list(map(int,input().split()))
    
    vk = [[] for x in range(m)]
    
    for i in v:
        vk[i%m].append(i)
        
    for i in range(m):
        
        print(f"{i} -> ",end='')
        
        for j in range(len(vk[i])):
            
            print(vk[i][j],end=' -> ')
            
        print("\\")
    if w != ct-1:
        print()
