n = int(input())

dic = {}

for i in range(n):
    a,b = map(str,input().split())
    dic[a] = int(b)
    

tn = n//3

vt = [{} for x in range(tn)]

dic = dict(sorted(dic.items(), key= lambda x: (-x[1])))

j = -1
for chave,valor in dic.items():
    j+=1
    
    
    vt[(j%tn)][chave] = valor

print(vt)
for i in range(tn):
    print(f'Time {i+1}')
    
    for chave,valor in (sorted(vt[i].items(),key= lambda x: (-x[1],x[0]))):
        print(f'{chave} {valor}')
    print()



