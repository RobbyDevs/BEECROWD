n,k = map(int,input().split())

v = []

for i in range(n):
    a,b = map(str,input().split())
    
    v.append([a,int(b)])
    
vf = [[] for x in range(k)]

v.sort(key= lambda x: (-x[1],x[0]))

j = -1
for i in range(len(v)):
    j+=1
    vf[j%k].append(v[i][0])

for i in range(len(vf)):
    print(f'Time {i+1}')
    for j in sorted(vf[i]):
        print(j)
    print()