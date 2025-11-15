for w in range(int(input())):
    
    m = []
    n = int(input())
    for i in range(n):
        m.append(list(map(int,input().split())))
    cap = int(input())
    res = int(input())
    dano = 0
    
    m.sort(key= lambda m: m[0]/m[1],reverse= True)

    for i in range(n):
        if cap < min(m[x][1] for x in range(i,len(m))):
            break
        else:  # >>>>>>>>>>> ERRO 5% NESTE BLOCO DE CODIGO!
            if cap >= m[i][1]:
                
                cap -= m[i][1]
                dano += m[i][0]
    
    
    if res - dano > 0:
        print('Falha na missao')
    else:
        print('Missao completada com sucesso')
        
