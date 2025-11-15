case = 0

while True:
    case += 1
    n, q = map(int, input().split())

    if n + q == 0:
        break

    print(f"CASE# {case}:")
    v = []
    for i in range(n):
        v.append(int(input()))
    
    maior = max(v)
    menor = min(v)
    
    dis = maior - menor + 1

    vf = [0 for x in range(dis+1)]

    for i in v:
        vf[i - menor] += 1

    vp = [0] * (dis + 2)
    
    for i in range(1, dis+2):
        vp[i] = vp[i - 1] + vf[i - 1]

    for i in range(q):
        alvo = int(input())

        if (alvo < menor) or (alvo > maior) or (vf[alvo - menor] == 0):
            print(f"{alvo} not found")
        else:
            pos = vp[alvo - menor] + 1
            print(f"{alvo} found at {pos}")
