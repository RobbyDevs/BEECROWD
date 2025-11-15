n = int(input())
t = 7

if n > 7:
    if n > 10:
        if n > 30:
            if n > 100:
                t = t + (n-100)*5
                n = 100
            t = t + (n-30)*2
            n = 30
        t = t + (n-10)
    
        
    
print(t)