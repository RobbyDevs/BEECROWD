v = []
v.append(int(input()))

for i in range(1,11):
    v.append(v[i-1]*2)
    print(f"N[{i-1}] = {v[i-1]}")