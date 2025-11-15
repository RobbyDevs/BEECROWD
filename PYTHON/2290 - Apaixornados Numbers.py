''while True:
    
    try:
        
    
        n = int(input())
        if n == 0:
            break
        
        v = sorted(list(map(int,input().split())))
        dic = {}
        for i in v:
            
            try:
                dic[i]+=1
            except KeyError:
                dic[i] = 1
        
        va = []
        for chave,val in dic.items():
            if val % 2 != 0:
                va.append(str(chave))
        
        print(' '.join(va))
    
    except EOFError:
        break
    ''