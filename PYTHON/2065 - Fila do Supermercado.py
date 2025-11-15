import sys
from heapq import *

input = sys.stdin.readline

fun,cli = map(int,input().split())
vfun = list(map(int,input().split()))
vcli = list(map(int,input().split()))

#tempo livre | ind | t/item
heap = [[0,i+1,vfun[i]] for i in range(fun)]

ans = 0
aux = []
heapify(heap)
for i in range(cli):
    #print(heap)
    heap[0][0]+=(heap[0][2]*vcli[i])
    aux = list(heappop(heap))
    heappush(heap,aux)
    

for i in heap:
    if i[0]>ans:
        ans = i[0]
    
print(ans)