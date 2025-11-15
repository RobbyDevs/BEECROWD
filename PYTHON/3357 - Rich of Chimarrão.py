n, l, g = map(float, input().split())
n = int(n)
v = list(map(str, input().split()))

r = int(l // g)  
sobra = l % g

indice = r % n 
print(f'{v[indice]} {sobra:.1f}')
