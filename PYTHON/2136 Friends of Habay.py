dic = {}
flag = 0
res = ''
while True:
    a = input()
    
    
    if a == "FIM":
        break
    a,b = map(str,a.split())
    
    dic[a] = b
    if flag == 0:
        
        if b == 'YES':
            res = a
            flag = 1

v = list(dic.items())

v.sort(key= lambda x: (-ord(x[1][0])))

for i in v:
    print(i[0])
    
print()
print("Amigo do Habay:")
print(res)