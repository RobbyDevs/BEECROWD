import sys
input = sys.stdin.readline

def solve(n,k):
    v = [x+1 for x in range(n)]
    k-=1
    ind = 0
    ex = 0
    while len(v)>1:
    
        if ind+k < len(v)-1:
            ind = ind+k
            del v[ind]
        else:
            ind = (ind+k) %len(v)
            del v[ind]
            

    print(v[0])
for i in range(int(input())):
    n,k = map(int,input().split())
    print(f"Case {i+1}: ",end='')
    solve(n,k)
    
    