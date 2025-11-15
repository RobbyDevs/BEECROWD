while True:
    try:
        n,m = map(int,input().split())
        
        v = list(map(int,input().split()))
        dic = {}
        for i in range(len(v)):
            try:
                dic[str(v[i])][0]+=1
                dic[str(v[i])][1].append(i+1)
                
            except KeyError:
                dic[str(v[i])]=[0,[]]
                dic[str(v[i])][0]+=1
                dic[str(v[i])][1].append(i+1)
        
        #print(dic)
        
        for i in range(m):
            freq, valor = map(int,input().split())
            valor = str(valor)
            
            try:
                if valor in dic:                    
                    print(dic[valor][1][freq-1])
                else:
                    print(0)
                    continue
            except IndexError:
                print(0)
    except EOFError:
        break