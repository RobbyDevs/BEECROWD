n = int(input())

for i in range (1,n+1):

    a,d,g = map(int,input().split())

    if (a >= 200 and a <= 300) and (d>=50) and (g>=150):
        print("Sim")
    else:
        print("Nao")