from sys import stdin
import heapq
input = stdin.readline



def solve(n,m,c,k):
    
    grafo = {}
    rotas = {x:1000 for x in range(c)}
    caminhosC = [0]*(c)
    
    aux = 0
    for i in range(m):
        u,v,p = map(int,input().split())
        #print("conectando",u,v)
        
    
        if u not in grafo:
            grafo [u] = [[p,v]]
        else:
            grafo[u].append([p,v])
        
        if v not in grafo:
            grafo [v] = [[p,u]]
        
        else:
            grafo[v].append([p,u])
            
        if u <c and v <c and abs(u-v) == 1:
            #print(r)
            #print(u)
            caminhosC[min(u,v)]= p
            
        
    # Somando Rotas
    aux = 0
    
    for i in range(len(caminhosC)-1,-1,-1):
        caminhosC[i]+=aux
        aux = caminhosC[i]
    
    
   
    # MONTANDO DIJKSTRA
    fila = grafo[k]
    heapq.heapify(fila)
    
    print("fila",fila)
    
    

    print(caminhosC)
    print()
    print(grafo)
    

while True:
    
    n,m,c,k = map(int,input().split())
    if n+m+c+k == 0:
        break
    
    solve(n,m,c,k)
    print("\n\n")