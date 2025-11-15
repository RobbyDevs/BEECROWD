v = []
a = 100

for i in range(a):
    v.append(float(input()))
    
for i in range(a):
    if v[i] <= 10:
        print(f'N[{i}] = {v[i]}')