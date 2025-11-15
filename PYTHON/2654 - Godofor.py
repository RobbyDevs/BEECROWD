v = []

for w in range(int(input())):
    
    a,b,c,d = map(str,input().split())
    

    v.append([a,[int(b),int(c),int(d)]])
    


v.sort(key= lambda x: (x[1][0],x[1][1],x[1][2],(x[0].lower())))

#print(v[len(v)-1][0])

vf = []
r = v[len(v)-1][0]

if v[len(v)-1][1][0] == v[len(v)-2][1][0]:
    if v[len(v)-1][1][1] == v[len(v)-2][1][1]:
        if v[len(v)-1][1][2] == v[len(v)-2][1][2]:
            x1 = v[len(v)-1][0]
            x2 = v[len(v)-2][0]
            
            if x1.lower() < x2.lower():
                r = x2
            else:
                r   = x1

print(r)