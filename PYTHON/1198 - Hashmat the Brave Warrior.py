while True:
    try:
        n,m = map(int,input().split())
        
        print(abs(n-m))
        
        
    except EOFError:
        break