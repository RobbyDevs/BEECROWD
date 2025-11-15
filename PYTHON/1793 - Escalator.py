while True:
    n = int(input())
    if n == 0:
        break
    v = list(map(int,input().split()))
    
    if n == 1:
        print(10)
        continue
    
    c = 0
    s = 0
    for i in range(n-1):
        if v[i+1]-v[i]>=10:
            c+=10
        else:
            c+= (v[i+1]-v[i])
            
    print(c+10)
    
