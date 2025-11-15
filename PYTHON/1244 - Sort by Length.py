for w in range(int(input())):
    
    v = list(map(str,input().split()))
    
    vf = [[] for x in range(50)]
    
    maxi = 0
    
    mini = 50
    for i in v:
        vf[len(i)-1].append(i)
        if len(i)> maxi:
            maxi = len(i)
        if len(i)<mini:
            mini = len(i)
        
    #print(vf)
    
    for i in range(maxi-1,mini-1,-1):
        if len(vf[i])>0:
            
            print(' '.join(vf[i]),end=' ')
            
    print(' '.join(vf[mini-1]))
    
    