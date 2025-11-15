import sys
ler = sys.stdin.readline

caso = 0
while True:
    caso += 1
    n = int(ler())
    if n == 0:
        break
    if caso > 1:
        print()
    
    vf = [[0, 0.0, 0, 0, i] for i in range(1, n+1)]

    q = n*(n-1)//2
    for ind in range(q):
        x,y,z,w = map(int,ler().split())
        x -= 1
        z -= 1

        if y > w:
            vf[x][0] += 2
            vf[x][2] += y
            vf[x][3] += w

            vf[z][0] += 1
            vf[z][2] += w
            vf[z][3] += y
        else:
            vf[z][0] += 2
            vf[z][2] += w
            vf[z][3] += y

            vf[x][0] += 1
            vf[x][2] += y
            vf[x][3] += w

    for i in vf:
        if i[3] > 0:
            i[1] = i[2]/i[3]

    vf.sort(key=lambda x: (-x[0], -x[1], -x[2], x[4]))

    print(f"Instancia {caso}")
    ans = []
    for i in vf:
        ans.append(i[4])
    print(*ans,sep=' ')