n = int(input())

v = []
for i in range(n):
    a,b = map(str,input().split())
    v.append([a,int(b)])
#print(v)
v.sort(key= lambda x: (-x[1],x[0]))


vt = [[] for x in range(n//3)]
#print(vt)
j = -1
for i in v:
    j+=1
    #print(j)
    vt[j%(n//3)].append(i)
    
for i in range(len(vt)):
    print(f'Time {i+1}')
    for j in range(len(vt[i])):
        print(f'{vt[i][j][0]} {vt[i][j][1]}')
    print()