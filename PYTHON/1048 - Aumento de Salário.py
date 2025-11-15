s = float(input())
r,d,t=0,0,0

if s >= 0 and s <= 400:
    d = s*0.15
    t = s*1.15
    r = 15
 
elif s>=400.01 and s <= 800:
    d = s*0.12
    t = s*1.12
    r = 12
elif s>= 800.01 and s <= 1200:
    d = s*0.10
    t = s*1.10
    r = 10
elif s>= 1200.01 and s <= 2000:
    d = s*0.07
    t = s*1.07
    r = 7
elif s > 2000:
    d = s*0.04
    t = s*1.04
    r = 4

print(f"Novo salario: {t:.2f}\nReajuste ganho: {d:.2f}\nEm percentual: {r} %")