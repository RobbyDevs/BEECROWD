import sys

dados = sys.stdin.read().split()
idx = 0

while idx < len(dados):
    n = int(dados[idx])
    m = int(dados[idx + 1])
    idx += 2

    ma = []
    for i in range(n):
        ma.append([])
        for j in range(m):
            ma[i].append([int(dados[idx]), 0])
            if ma[i][j][0] == 1:
                 ma[i][j][1] = 1
            idx += 1
    #print(ma)
    ans =[]
    flag2 = 0

    for i in range(n):
        for j in range(m):
            if ma[i][j][1] == 0:
                flag = 0

                # >
                if j < m - 1:
                    if ma[i][j + 1][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i][j + 1][1] = 1

                # v
                if i < n - 1:
                    if ma[i + 1][j][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i + 1][j][1] = 1

                # <
                if j > 0:
                    if ma[i][j - 1][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i][j - 1][1] = 1

                # ^
                if i > 0:
                    if ma[i - 1][j][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i - 1][j][1] = 1

                # ^>
                if i > 0 and j < m - 1:
                    if ma[i - 1][j + 1][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i - 1][j + 1][1] = 1

                # v>
                if i < n - 1 and j < m - 1:
                    if ma[i + 1][j + 1][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i + 1][j + 1][1] = 1

                # <v
                if i < n - 1 and j > 0:
                    if ma[i + 1][j - 1][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i + 1][j - 1][1] = 1

                # <^
                if i > 0 and j > 0:
                    if ma[i - 1][j - 1][0] >= ma[i][j][0]:
                        ma[i][j][1] = 1
                        flag = 1
                    else:
                        ma[i - 1][j - 1][1] = 1

                if flag == 0:
                    ans.append(f"{i + 1} {j + 1}")
                    flag2 = 1

    if flag2 == 0:
        ans.append("-1")
    #print(ans)

    ans.append("")
    sys.stdout.write("\n".join(ans) + "\n")