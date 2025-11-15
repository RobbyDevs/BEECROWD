n = int(input())

for i in range (1,n+1):
    
    p = 1
    x = int(input())

    for j in range (1,x+1):
        p = p*2
    
    print(f"{p//12000} kg")
