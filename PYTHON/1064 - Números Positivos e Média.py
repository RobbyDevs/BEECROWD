m=x=c=0
for i in range(0,6):
    x = float(input())

    if x >0:
        c+=1
        m = m+x
    

print(f"{c} valores positivos\n{(m/c):.1f}")