n,l,d = map(int,input().split())

qt = n*d


print(qt)
vz = qt/(l*1000)
vvz = qt//(l*1000)

if abs(vz-vvz) !=0:
    vvz+=1
print(vvz*l)