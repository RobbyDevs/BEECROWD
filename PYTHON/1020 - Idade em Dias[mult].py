d = int(input())
a,m = 0,0

a = d//365

m = (d % 365) // 30

dia = (d % 365) % 30


print(f"{a} ano(s)\n{m} mes(es)\n{dia} dia(s)")