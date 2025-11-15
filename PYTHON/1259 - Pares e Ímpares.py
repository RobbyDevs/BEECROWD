n = int(input())
#leitura do valor n

val = [int(input()) for x in range(0,n)]
# preenchimento do vetor val de tamanho n, os valores sao lidos.

valP = [val[y] for y in range(0,(len(val))) if val[y]%2 == 0]
# valP eh o vetor que armazenarah os valores pares.
# valP serah preenchido com: val[y] sempre que esse valor presente em val seja par.

val = [val[y] for y in range(0,(len(val))) if val[y]%2 > 0]
#val agora sera o vetor que armazenarah os valores impares.

valP.sort()
val.sort()
val.reverse()

for i in range(0,(len(valP))):
    print(valP[i])

for z in range(0,(len(val))):
    print(val[z])