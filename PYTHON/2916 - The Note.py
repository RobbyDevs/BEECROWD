import sys
input  = sys.stdin.readline

while True:
    v = []
    linha = input()
    if linha == '':
        break
    try: 
        n,k = map(int,linha.split())
    except:
        n = int(linha)
        k = int(input())
        
    while len(v)<n:
        v.extend(list(map(int,input().split())))
    
    v.sort()
    print(sum(v[n-k:])%((10**9)+7))
        
        
"""
10 5
1 2 3 4 5 6 7 8 9 10
5 2
1 5 2 4 3
17 5
17 15 11 11 9 7 5 3 3 1 2 4 6 8 10 12 14

"""