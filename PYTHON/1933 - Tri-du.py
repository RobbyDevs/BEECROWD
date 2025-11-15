v = list(map(int,input().split()))

if len(list(set(v))) < 2:
    print(v[0])
else:
    print(max(v))