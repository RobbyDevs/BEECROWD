import sys
sys.stdin.readline

v,n = input().split()
n = int(n)

texto = []


for i in range(len(v)):
    if i == 0 :
        if v[i] == '?':
            texto.append('1')
        else:
            texto.append(v[i])
    else:
        if v[i] == "?":
            texto.append('0')
        
        else:
            texto.append(v[i])
    
numero = int(''.join(texto))
print(numero)

if numero%n ==0:
    print(numero)
else:
    ciclo = {}
    
    for i in range(1,6):
        ciclo[str(n**i)[-1]] = 1
    #print(ciclo)
            

    if v[-1] not in ciclo:
        print("*")
    
    else:
        base = ((numero//n)*n)+n

        mod = base%n


        while mod !=0:
            
            base+=n
            mod = base%n
        print(base)