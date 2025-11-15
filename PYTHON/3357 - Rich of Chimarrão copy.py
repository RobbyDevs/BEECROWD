n,l,q = map(float,input().split())
v = list(map(str,input().split()))
p = 0
while l-q >0:
    l = l-q
    p+=1

print(f'{v[int(p%n)]} {l:.1f}')