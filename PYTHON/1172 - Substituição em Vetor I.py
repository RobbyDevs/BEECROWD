x = []
a = 0

for i in range(0,10):
    a = int(input())
    if a <= 0:
        x.append(1)
    else:
        x.append(a)
    print(f"X[{i}] = {x[i]}")