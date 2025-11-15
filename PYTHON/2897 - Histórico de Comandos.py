import sys

input = sys.stdin.readline

def solve(n):
    dic = {}
    pilha = [0]
    v = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if v[i] not in dic:
            ans+=v[i]+len(pilha)-1
            dic[v[i]]=len(pilha)
            pilha.append(v[i])
        else:
            ans+= len(pilha)-dic[v[i]]
            dic[v[i]] = len(pilha)
            pilha.append(v[i])
        
    print(ans)
    
while True:
    n = int(input())
    if n == 0:
        break
    
    solve(n)
