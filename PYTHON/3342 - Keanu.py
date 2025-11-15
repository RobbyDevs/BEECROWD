n = int(input())

p = (n*n)//2

if n % 2 > 0:
    print(f"{p+1} casas brancas e {p} casas pretas")
else:
    print(f"{p} casas brancas e {p} casas pretas")