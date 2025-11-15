n = int(input())
fila = list(map(str,input().split()))
m = int(input())
dxfila = list(map(str,input().split()))

for i in range(0,m):
    for j in range(0,n):
        if dxfila[i] == fila[j]:
            fila.pop(j)
            break
print(' '.join(fila))

#Se for para remover valores de um vetor, utilizar break antes do laco chegar ao final do mesmo