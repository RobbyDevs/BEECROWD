while True:
    n = int(input())
    if n == 0:
        break
    f = inc = 0
    
    while f+inc <n:
        inc+=1
        f+=inc
    print(f'{f} {n-f}')