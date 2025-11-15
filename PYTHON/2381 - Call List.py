n,k = map(int,input().split())

v = []

for i in range(n):
    v.append(input())
    
print(sorted(v)[k-1])
