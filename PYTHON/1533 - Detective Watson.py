while True:
    n = int(input())
    
    if n == 0:
        break
        
    v = list(map(int,input().split()))
    
    mma = max(v)
    mmi = 0
    for i in v:
        if i > mmi and i < mma:
            mmi = i
    print(v.index(mmi)+1)
    