vd,vh,vm,vs = 0,0,0,0

d0 = int(input().split()[1])
h0,m0,s0 = map(int,input().split(' : '))

df = int(input().split()[1])
hf,mf,sf = map(int,input().split(' : '))

if sf >= s0:
    vs = sf - s0
else:
    vs = 60 - abs(sf-s0)
    vm = -1
    

if mf >= m0:
    vm += mf-m0

else:
    vm += 60 - abs(mf-m0)
    vh = -1

if hf >= h0:
    vh += hf - h0

else:
    vh += 24 - abs(hf - h0)
    vd = - 1

    if vm == -1:
        vh -= 1
        vm = 59
    elif vh == -1:
        vd -= 1
        vh = 23

vd += df - d0

print(f"{vd} dia(s)\n{vh} hora(s)\n{vm} minuto(s)\n{vs} segundo(s)")