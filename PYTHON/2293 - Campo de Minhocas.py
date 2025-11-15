l,c = map(int,input().split())

G = [list(map(int,input().split())) for x in range(l)]
# MATRIZ COMPRESSA

if len(G[0]) == 1:

    f = [sum([sum(G[i]) for i in range(0,len(G))])]

else:
    f = [max([sum(G[i][0:c]) for i in range(l)]), max([sum([G[i][j] for i in range(l)]) for j in range(c)])]

print(max(f))
    