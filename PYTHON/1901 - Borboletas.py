n = int(input())
dic = {}
m = []
for i in range(n):
    va = list(map(int,input().split()))
    
    for j in range(n):
        dic[(i+1,j+1)] = va[j]
    m.append(va)

s = set()
for i in range(n*2):
    a,b = map(int,input().split())
    s.add(dic[(a,b)])

print(len(s))