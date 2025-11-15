case = 0

while True:
    case +=1
    n,q = map(int,input().split())
    
    if n+q == 0:
        break
    
    print(f"Case# {case}:")
    ##########
    
    v = []
    
    for i in range(n):
        v.append(int(input()))
        
    maior = max(v)
    menor = min(v)
    
    vf = [0 for x in range((maior-menor)+2)]
    
    for i in v:
        vf[i-menor]+=1

    for i in range(q):
        alvo = int(input())
        if( (alvo > maior) or (alvo < menor)):
            
            print(f'{alvo} not found')
            
        else:
            if vf[alvo-menor] == 0:
                print(f'{alvo} not found')
            else:
                print(f"{alvo} found at {sum(vf[:alvo-menor])+1}")
            
        