for w in range(int(input())):
    
    x,n = map(int,input().split())
    

    if x %2 == 0: x+=1
    y = x+(2*(n-1))
    
    print(((x+y)*n)//2)