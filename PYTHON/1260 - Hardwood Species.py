nn = int(input())
input()
for w in range(nn):
    
    dic = {}
    n = 0
    while True:
        try:
            
            a = input()
            if a =='':
                break
        except EOFError:
            break
        
        try:
            dic[a]+=1
        except KeyError:
            dic[a] = 1
        n+=1
        
    for chave,valor in sorted(dic.items()):
        print(f'{chave} {((valor/n)*100):.4f}')
    
    if w < (nn-1):
        print() 