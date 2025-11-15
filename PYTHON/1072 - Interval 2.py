n = int(input())

i = 0
o = 0
for w in range(n):
    if int(input()) in range(10,21):
        i+=1
    else:
        o+=1

print(f'{i} in')
print(f'{o} out')