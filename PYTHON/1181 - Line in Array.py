l = int(input())
nn = 12
s = input()

m = []

for i in range(nn):
    ll = []
    
    for j in range(nn):
    
        ll.append(float(input()))
    m.append(ll)
    

if s == "M":
    print(sum(m[l])/nn)
    
elif s == "S":
    print(sum(m[l]))