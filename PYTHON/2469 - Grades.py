n = int(input())

v = list(map(int,input().split()))

vf = [0 for x in range(100)]

for i in v:
    vf[i-1]+=1
    
mai = max(vf)


va = []

for i in range(99,-1,-1):
    if vf[i] == mai:
        print(i+1)
        break
        
