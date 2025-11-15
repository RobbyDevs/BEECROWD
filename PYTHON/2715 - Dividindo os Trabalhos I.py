import sys

input = sys.stdin.readline


    
def solve(n):
    v = list(map(int,input().split()))
    
    
    vd = sum(v)
    ve = 0
    ans = abs(ve-vd)    
    
    for i in range(n):
        ve +=v[i]
        vd -= v[i]
        ans = min(ans,abs(ve-vd))
        
    print(ans)
    
   # print(ve)
   # print(vd)

while True:
    n = input()
    
    if n =='':
        break
    solve(int(n))
   # print('^^^^')
    