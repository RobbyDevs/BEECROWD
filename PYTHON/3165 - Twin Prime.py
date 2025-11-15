v = [2,3]
vp = []

m = int(input())

for i in range((int(m*0.8)),m+1,6):
    v.append(i)
    if i+2<=m:
        v.append(i+2)
    
for n in v:
    
    p = 5
    
    while p*p <= n:
        if(n%p ==0 or n%(p+2) ==0):
            break
        p+=6
    else:
        vp.append(n)

v = []

for i in range(len(vp)-2,-1,-1):
    if vp[i+1]-vp[i]==2:
        print(vp[i],vp[i+1])
        break