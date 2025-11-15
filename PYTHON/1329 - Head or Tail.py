while True:
    n = int(input())
    
    if n == 0:
        break
    
    m = sum(list(map(int,input().split())))
            
    print(f"Mary won {m} times and John won {n-m} times")
    