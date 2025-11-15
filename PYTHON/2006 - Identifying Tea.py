n = int(input())
c = 0
for i in list(map(int,input().split())):
    if i == n:
        c+=1
        
print(c)