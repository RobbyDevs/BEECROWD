n = int(input())


v = [1 for x in range(n+1)]

v[0] = v[1] = 0
va = []
p = 2
while p*p <= n:
    
    if v[p] == 1:
        for i in range(p*p,n+1,p):
            v[i] = 0
    p+=1

for i in range(n):
    if v[i] == 1:
        print(i,end=',')

print()