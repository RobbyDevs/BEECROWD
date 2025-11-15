while True:
    n = int(input())
    if n == 0:break
    
    v = 'NLSO'
    
    d = 0
    for i in input():
        if i =='D':
            d+=1
            
    r = (d-(n-d))%4
    print(v[r])
    
    