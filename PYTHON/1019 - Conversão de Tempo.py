t = int(input())
h,m,s = 0,0,0

while t >= 60:

    if t >= 3600:
        t -= 3600
        h += 1

    elif t >= 60:
        t -= 60
        m += 1


print(f"{h}:{m}:{t}")