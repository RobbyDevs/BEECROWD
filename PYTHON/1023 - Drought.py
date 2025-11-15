from math import floor
from decimal import Decimal,ROUND_DOWN
while True:
    n = int(input())
    
    if n == 0 :
        break
    
    c = 1
    v = []
    for i in range(n):
        v.append(list(map(int,input().split())))
        
    v.sort(key = lambda v: (v[0],v[1]))
    
    print(f'Cidade# {c}:')
    
    media = p = 0
    for j in range(n):
        print(f'{v[j][0]}-{floor((v[j][1])//v[j][0])}',end=' ')
        media += v[j][1]
        p += v[j][0]
    print()
    
    media = Decimal(media / p)
    print(f'Consumo medio: {media.quantize(Decimal("0.01"), rounding=ROUND_DOWN)} m3.')
    if c <n-1:
        print()
    c+=1