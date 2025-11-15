n,k = map(int,input().split())

v = list(map(int,input().split()))

v.sort()
print(v)
print(sum(v[n-k:]))