while True:
    n,a,b = map(int,input().split())

    if a == n and b == a and n == 0:
        break
    else:
        if a%b == 0 or a%b == 0:
            c = min(a,b)
            c = n//c
        else:
            c = (n/a + n/b) - (n/(a*b))
            
            
        
    print(c)