v = []
for w in range(int(input())):
    nome, o,p,b = map(str,input().split())
    
    o = int(o)
    p = int(p)
    b = int(b)
    
    v.append([nome,[o,p,b]])
v.sort(key= lambda x: (-x[1][0],-x[1][1],-x[1][2],x[0]))

for i in range(len(v)):
    print(f'{v[i][0]} {v[i][1][0]} {v[i][1][1]} {v[i][1][2]}')