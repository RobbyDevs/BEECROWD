for i in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    c = 0
    
    
    v1 = sorted(v, reverse= True)
    for i in range(n):
        if v1[i] == v[i]:
            c+=1
    print(c)