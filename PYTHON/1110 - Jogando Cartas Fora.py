import sys
from collections import deque

ler = sys.stdin.readline

while True:
    n = int(ler())
    
    if n == 0:
        break
    else:
    
        v = deque(x for x in range(1,n+1))
        va = deque()
        
        while len(v)>1:
                va.append(v[0])
                v.popleft()
                v.append(v.popleft())

        
        print("Discarded cards:",end=' ')
        print(*va,sep=', ')
        print(f'Remaining card: {v[0]}')