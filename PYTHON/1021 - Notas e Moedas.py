v,c = map(float,input().split('.'))

n100 = int(v // 100)

n50 = int((v%100)//50)
n20 = int(((v%100)%50) // 20)
n10 = int((((v%100)%50)%20)//10)
n5  = int(((((v%100)%50)%20)%10)//5)
n2  = int((((((v%100)%50)%20)%10)%5)//2)

c100= int((((((v%100)%50)%20)%10)%5)%2)

c50 = int((c%100)//50)
c25 = int(((c%100)%50) // 25)
c10 = int((((c%100)%50)%25)//10)
c5  = int(((((c%100)%50)%25)%10)//5)
c1  = int((((((c%100)%50)%25)%10)%5))



print(f"NOTAS:\n{n100} nota(s) de R$ 100.00\n{n50} nota(s) de R$ 50.00\n{n20} nota(s) de R$ 20.00\n{n10} nota(s) de R$ 10.00\n{n5} nota(s) de R$ 5.00\n{n2} nota(s) de R$ 2.00")
print(f"MOEDAS:\n{c100} moeda(s) de R$ 1.00\n{c50} moeda(s) de R$ 0.50\n{c25} moeda(s) de R$ 0.25\n{c10} moeda(s) de R$ 0.10\n{c5} moeda(s) de R$ 0.05\n{c1} moeda(s) de R$ 0.01")