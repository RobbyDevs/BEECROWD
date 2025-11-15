m,n = map(int,input().split())
dic = {}
for w in range(m):
    chave,valor = input().split()
    dic[chave] = int(valor)

for i in range(n):
    v = []
    s = 0
    
    while True:
        
        a = input()
        if a == ".":
            break
        v.append(a.split())
    
    for x in range(len(v)):
        for y in range(len(v[x])):
            try:
                s+= dic[v[x][y]]
            except KeyError:
                pass
    print(s)
    
