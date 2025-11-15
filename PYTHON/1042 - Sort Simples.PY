listaD = [int(x) for x in input().split()]
listaO = sorted(listaD)

for i in range(0,len(listaO)):

    print(f"{listaO[i]}")

print("")

for i in range(0,len(listaD)):

    print(f"{listaD[i]}")