import sys
input = sys.stdin.readline

def solve(n,k,m):
    v = [x+1 for x in range(n)]
    k-=1
    m-=1
    ex = []
    I = 0
    J = len(v)-1

    while len(v)>2:
        print("v:",v)
        print("ex:",ex)
        if I + k >= len(v):
            I = ((I+k)%len(v))-1
            
        else:
            I = I+k
        
        print(J,"-",m)
        if J-m <0:
            J = (J-m)%len(v)
        else:
            J = J-m
            
        print('i:',I,v[I])
        print('j:',J,v[J])
        
        if I == J:
            ex.append([v[I]])
            
            del v[I]
            J-=1
            
        else:
            ex.append([v[I],v[J]])
            del v[max(I,J)]
            del v[min(I,J)]
            J-=1
            if I<J:
                J-=1
            

    print(v)
    print(ex)
    print(I,J)
    
"""    for i in range(len(ex)-1):
        z = ''
        if ex[i] <100:
            z = " "
        if ex[i] <10:
            z= "  "
        print(f"{}")
            
        """
        
#ERRO NA HORA DE CALCULAR O ULTIMO PAR. POSSIVELMENTE UMA SUBTRACAO DE INDICE ERRADA
    
while True:
    n,k,m = map(int,input().split())
    if n+k+m == 0:
        break
    
    solve(n,k,m)
    
    
    
    
"""

4 9 3 2
8 5 1 6

"""