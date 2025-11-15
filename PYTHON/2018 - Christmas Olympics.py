dic = {}
while True:
    try:
        input()
        a = input()
        b = input()
        c = input()
        v = [a,b,c]
        

        for i in range(3):
            try:
                dic[v[i]][i] +=1
        
            except KeyError:
                
                dic[v[i]] = [0,0,0]
                dic[v[i]][i] +=1
                
        
    except EOFError:
        
        dic = sorted(dic.items(), key= lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))
        print("Quadro de Medalhas")
        for key,value in dic:
            print(f"{key} {value[0]} {value[1]} {value[2]}")
        
        break
