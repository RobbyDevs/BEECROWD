v = []
a = 20

for i in range(a):
    v.append(int(input()))
    
j = a -1
for i in range(a//2):
    v[i],v[j] = v[j],v[i]
    j-=1
for i in range(a):
    print(f'N[{i}] = {v[i]}')