n = int(input())

v = sorted(list(map(int,input().split())))

if v [0] == 2:
    print(1)
    
elif v[n-2] == n-1:
    print(n)
    
else:
    
    for i in range(n-2):
        if v[i+1]-v[i]>1:
            print(i+2)