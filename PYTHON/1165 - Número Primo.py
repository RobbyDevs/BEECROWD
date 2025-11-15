n = int(input())
for i in range(0,n):
    v = int(input())
    text = "eh primo"

    for j in range(2,((v//2)+1)):
    
        if v % j == 0:
            text = "nao eh primo"
            break
            
    print(f"{v} {text}")