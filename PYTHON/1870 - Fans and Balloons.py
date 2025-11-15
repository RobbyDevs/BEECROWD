
def solve(l,c,p):
    
    ma =[]
    for i in range(l):
        ma.append(input())
        
    
    popl = popc = 0
    sl = sc= 0
    flag = 0
    for i in range(c):
        e=d=0
        for j in range(l):
            if ma[j][i] !=0:
                e = ma[j][i]
            else:
                for k in range(i+1,c):
                    if ma[j][i] !=0:
                        d = ma[j][i]

                try:
                    if ma[i-(abs(e-d))][j] !=0:
                        popl= j
                        popc = i
                        flag = 1
                        
                        break
                except IndexError:
                    popl= j
                    popc = i
                    flag = 1
                    break
        else:
            sl = j
            sc = i
            flag = 0
            break
            
    if flag == 0:
        return f"OUT {sc}"
    else:
        return f"BOOM {popl} {popc}"
                        
    


while True:
    l,c,p = map(int,input().split())
    if l+c+p == 0:
        break
    
    print(solve(l,c,p))
    

    
