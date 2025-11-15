def solve():
    ma = []
    v = [1,2,3,4,5,6,7,8,9]
    va = []
    flag = True
    
    for i in range(9):
        va = list(map(int,input().split()))
        ma.append(va)
        if sorted(va) != v:
            flag = False
            
    for i in range(9):
        va = []
        for j in range(9):
            va.append(ma[j][i])

        if sorted(va) != v:
            flag = False
            break
    
    if flag == False:
        return "NAO"
    else:

        flag = True
        for i in range(0,9,3):
            for j in range(0,9,3):
                va = []
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        va.append(ma[x][y])
        
        
                va.sort()
                if va != v:
                    flag = False
                    break
                
            if flag == False:
                break
        
        if flag == False:
            return "NAO"
        else:
            return "SIM"
        
    
    
    
    


for w in range(int(input())):
    print('Instancia',w+1)
    ans = solve()
    print(ans)
    print()