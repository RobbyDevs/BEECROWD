caso = 0
while True:
    caso+=1
    try:
        n = int(input())
        if n == 0:
            break
        
        vr = []
        for i in range(n):
            nome = input()
            
            v = list(map(int,input().split()))
            
            v.sort()
            v.pop(0)
            v.pop(len(v)-1)
            soma = sum(v)
            
            vr.append([soma,nome,1])
        
        
        vr.sort(key=lambda x: (-x[0],x[1]))
        col = 1
        s = 0
        
        for i in range(1,n):
            if vr[i-1][0]==vr[i][0]:
                vr[i][2] = col
            else:
                vr[i][2] = i+1
                col = i+1
        
        print('Teste',caso)
        for i in range(n):
            print(vr[i][2],vr[i][0],vr[i][1])
        print()
    except EOFError:
        break
    

