n = int(input())

v=list(map(int,input().split()))

v.sort()
if n % 2 ==0:
    
    print((v[(n//2)-1]+v[(n//2)])//2)
else:
    print(v[n//2])