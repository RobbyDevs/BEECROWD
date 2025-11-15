cc = 0

v = list(map(int,input().split()))

for i in range(len(v)-1):
    if v[i] < v[i+1]:
        cc+=1

if cc==0:
    print("D")
elif cc == len(v)-1:
    print("C")
else:
    print("N")