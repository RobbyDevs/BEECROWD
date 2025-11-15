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
    
    # Cria lista com [pontos, media, feitos, recebidos, id]
    times = [[0, 0.0, 0, 0, i] for i in range(1, n+1)]

    qtd_jogos = n * (n - 1) // 2
    for _ in range(qtd_jogos):
        x, y, z, w = map(int, ler().split())
        x -= 1
        z -= 1

        if y > w:
            times[x][0] += 2
            times[x][2] += y
            times[x][3] += w

            times[z][0] += 1
            times[z][2] += w
            times[z][3] += y
        else:
            times[z][0] += 2
            times[z][2] += w
            times[z][3] += y

            times[x][0] += 1
            times[x][2] += y
            times[x][3] += w

    for time in times:
        if time[3] > 0:
            time[1] = time[2] / time[3]  # média de gols feitos/sofridos

    # Ordena: pontos desc, média desc, feitos desc, id asc
    times.sort(key=lambda x: (-x[0], -x[1], -x[2], x[4]))

    print(f"Instancia {caso}")
    print(' '.join(str(t[4]) for t in times))
