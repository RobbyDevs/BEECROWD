v = int(input())

s,a,b,c,d,e,f = 0,0,0,0,0,0,0
print(v)

while v >= 1:

    if v>=100:
        v = v - 100
        s = s + 1
    elif v>=50:
        v = v - 50
        a = a + 1

    elif v>=20:
        v = v - 20
        b = b + 1

    elif v >= 10:
        v = v - 10
        c = c + 1


    elif v>=5:
        v = v - 5
        d = d + 1

    elif v >= 2:
        v = v - 2
        e = e + 1

    elif v >= 1:
        v = v - 1
        f = f + 1


print(f"{s} nota(s) de R$ 100,00")
print(f"{a} nota(s) de R$ 50,00")

print(f"{b} nota(s) de R$ 20,00")
print(f"{c} nota(s) de R$ 10,00")

print(f"{d} nota(s) de R$ 5,00")
print(f"{e} nota(s) de R$ 2,00")

print(f"{f} nota(s) de R$ 1,00")