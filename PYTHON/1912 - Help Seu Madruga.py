import sys
ler = sys.stdin.readline

def cArea(corte):
    a = 0
    
    for i in range(int(corte),len(vf)):
        if vf[i]>0 and i>corte:
            a += (i-corte)*vf[i]
            
    return a


def BB(e,d,meio):
    area = cArea(meio)

    while abs(area-a) > 0.00001:
        #print(area,meio)
        
        if area < a:
            d = meio
        
        elif area > a:
            e = meio
        meio = (e+d)/2
        area = cArea(meio)
    print(f"{meio:.4f}")
         



while True:
    n,a = map(int,ler().split())
    if n+a ==0:
        break
    
    v = list(map(int,ler().split()))
    mai = max(v)
    vf = [0]*(mai+1)
    
    for i in v:
        vf[i]+=1
    #print(vf)
    
    soma = sum(v)
    if soma == a:
        print(":D")
    elif soma<a:
        print("-.-")
        
    else:
        esq = 0
        dir = max(v)
        meio = (esq+dir)/2
        
        BB(esq,dir,meio)
