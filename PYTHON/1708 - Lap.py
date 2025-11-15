x,y = map(int,input().split())
d = y-x
c = 1
while d < y:
    d += y-x
    c+=1
    
print(c)