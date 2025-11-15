dic = {}
while True:
    try:
        
        matou, morreu = input().split()
        
        try:
            dic[matou][1]+=1    
        except KeyError:
            dic[matou] = [1,1]
            
        try:
            dic[morreu][0]=0
        except KeyError:
            dic[morreu] = [0,0]
            dic[morreu][0]=0
        
        
            
    except EOFError:
        #print(dic)
        v= []
        
        for chave in dic.keys():
            if dic[chave][0] == 1:
                v.append([chave,dic[chave][1]])
                
        v.sort(key= lambda x: x[0])
        
        #print(v)
        print('HALL OF MURDERERS')
        
        for i in range(len(v)):
            print(*v[i],sep=' ')
        break