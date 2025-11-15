x = int(input())

while True:
    y = int(input())
    if y>x:
        break

s = x
c = 1
ad = x
while s <=y:
    ad+=1
    s +=ad
    c+=1
    #print(s)
print(c)