v = list(map(int,input().split()))

v.sort()
r = ''

if v[2] >= v[0]+v[1]:
    r = 'n'
    
else:
    if v[2]**2 == (v[0]**2)+(v[1]**2):
        r = 'r'
    elif v[2]**2 > (v[0]**2)+(v[1]**2):
        r = 'o'
    elif v[2]**2 < (v[0]**2)+(v[1]**2):
        r = 'a'
    
print(r)