d = int(input())
a,m = 0,0
while d >= 30:
    if d >= 365:
        d -= 365
        a = a + 1

    elif d > 30:
        d -= 30
        m = m + 1

print(f"{a} ano(s)\n{m} mes(es)\n{d} dia(s)")