linha = 0
while True:
    linha +=1
    
    n = int(input())
    if ( n == 0):
        break
    if linha >1:
        print()
    v = []
    for i in range(n):
        a = input()
        b,c = map(str,input().split())
        
        v.append([a,b,c])
        
    v.sort(key= lambda x: (x[1],-ord(x[2]), x[0]))
    
    for i in range(n):
        print(f'{v[i][1]} {v[i][2]} {v[i][0]}')
    