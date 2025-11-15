import sys
ler = sys.stdin.readline


while True:
    n,m = map(int,ler().split())
    if n==0 and m == 0:
        print(0,0)
        break
    v = []
    for i in range(n):
        a = int(ler())
        if a >=0:
            
            b = a%m
        else:
            b = abs(a)%m *-1
        
        v.append([a,b])
        
        
    v.sort(key= lambda x: (x[1],-(x[0]%2),(-x[0] if x[0]%2 == 1 else x[0])))
    
  
    print(n,m)
    for i in v:
        print(i[0])
        
