import sys

input = sys.stdin.readline
s = ['F','A','C','E']

v = []
ans = 0
for i in range(int(input())):
    if len(v) == 0:
        v.append(s)
        
        
    va = input().split()
    vb = list(reversed(va))

    if vb==v[-1]:
        ans +=1
        v.pop()
        
    else:
        v.append(va)
print(ans)
