import sys
input = sys.stdin.readline


def solve(n,p):
    pilhas = []
    for i in range(p):
        v = list(map(int,input().split()))
        t = v[0]
        pilhas.append(v[1:])
        
    inv = 0
    ans = 0
    alt = 0
    for i in range(p):
        for j in range(len(pilhas[i])):
            if pilhas[i][j] == 1:
                inv = i
                ans = len(pilhas[i])-j-1
                alt = j

    
    esq = dir = 0
    for i in range(inv-1,-1,-1):
        if len(pilhas[i])> alt:
            esq+= len(pilhas[i])-alt
        else:
            break
            
            
    for i in range(inv+1,p):
        if len(pilhas[i]) > alt:
            dir += len(pilhas[i])-alt
        else:
            break
    ans += min(esq,dir)
    print(ans)        


while True:
    n,p = map(int,input().split())
    if n+p == 0:
        break
    solve(n,p)
