while True:
    n = int(input())
    
    if n == 0:
        break
    
    aa = bb = 0
    for i in range(n):
        a,b = map(int,input().split())
        
        if a >b:
            aa+=1
        elif a<b:
            bb+=1
        
    print(f'{aa} {bb}')

