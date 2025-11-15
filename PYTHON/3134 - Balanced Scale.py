a,b,c,d = [float(input()) for x in range(4)]


v = [a,b,c,d]

v.sort()
print(v)
l = len(v)
for i in range(l):
    if v[i]<v[i:l]:
        