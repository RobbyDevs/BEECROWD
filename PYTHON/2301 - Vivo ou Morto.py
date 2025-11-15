import sys
input = sys.stdin.readline

def solve(r):
    v = list(map(int, input().split()))
    for i in range(r):
        vr = list(map(int, input().split()))
        n, val = vr[0], vr[1]

        for j in range(n-1,-1,-1):
            if vr[j+2]!= val:  
                del v[j]
    print(v[0])

caso = 0
while True:
    caso += 1
    p, r = input().split()
    if p + r == "00":
        break
    print(f"Teste {caso}")
    solve(int(r))
    print()
