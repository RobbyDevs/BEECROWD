for w in range(int(input())):
    v = input()
    
    a,x,b = int(v[0]),v[1],int(v[2])
    v ='abcdefghijklmnopqrstuvwxyz'
    r = 0
    if a == b:
        r = a*a
        
    else:
        if x in v:
            r = a+b
        else:
            r = b-a
    
    print(r)
    