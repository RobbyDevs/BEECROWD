while True:
    
    a,b = map(str,input().split())
    if a == b and a == '0':
        break
   
    
    else:
        
        while len(a) > 1:
            a = [str(x) for x in (str(sum([int(y) for y in a])))]
        
        while len(b) > 1:
            b = [str(x) for x in (str(sum([int(y) for y in b])))]
        a,b = a[0],b[0]
        
        if int(a) > int(b):
            print(1)
        elif int(a) < int(b):
            print(2)
        else:
            print(0)