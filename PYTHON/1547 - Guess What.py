for w in range(int(input())):
    
    n, k = map(int,input().split())
    
    v = list(map(int,input().split()))
    
    ind = 0
    dif = 1000000
    con = False
    indif = 0
    
    for i in range(len(v)):
        if v[i] == k:
            ind = i
            con = True
            break
        
    if con == True:
        print(ind+1)
    else:
        for i in range(len(v)):
            if abs(k-v[i])<dif:
                dif = abs(k-v[i])
                ind = i
                
        print(ind+1)

    