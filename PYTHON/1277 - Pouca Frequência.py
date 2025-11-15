nomes = []
a=p=l=0
for i in range(0,(int(input()))):
    n = int(input())
    nomes = list(map(str,input().split()))
    reg = list(map(str,input().split()))
    
    rep = []
    for i in range(0,len(reg)):
        l = len(reg[i])
        for j in range(0,len(reg[i])):
            if reg[i][j] == "P":
                p+=1
            elif reg[i][j] == "A":
                a+=1
            else:
                l=l-1
        if (p/l) < 0.75:
            rep.append(nomes[i])
        
        a=p=l=0
    rep = " ".join(rep)
    print(rep)
                