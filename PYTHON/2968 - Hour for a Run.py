from math import ceil

k, n = map(int,input().split())

volta1 = ceil((n*k)/10)

soma = (n*k)//10


for i in range(9):
    
    print(volta1 + (soma*i))