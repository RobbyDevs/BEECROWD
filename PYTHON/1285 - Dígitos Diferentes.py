

n,m = map(int,input().split())
ntxt,mtxt = str(n),str(m)

val = [str(x) for x in range(n,m+1)]

for num in val:
    for caracter in val[num]:
        print(caracter)


#verificar uma forma de imprimir cada caracter de cada indice do vetor val[]=