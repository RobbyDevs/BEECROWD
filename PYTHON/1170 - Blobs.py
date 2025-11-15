n = int(input())
x=c=0
for i in range(0,n):
    x = float(input())

    while x > 1:
        x = x/2
        c+=1
    print(f"{c} dias")
    c=0