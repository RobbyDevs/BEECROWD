v = []


for i in range(1,101):
    v.append(int(input()))
a = max(v)

print(a)
print(v.index(a)+1)