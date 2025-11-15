while True:
    try:
        a,b = map(str,input().split("+"))
        b,c = map(str,b.split("="))
        
        try:
            int(a)
        except ValueError:
            print(int(c)-int(b))
            continue
        try:
            int(b)
        except ValueError:
            print(int(c)-int(a))
            continue
        
        print(int(a)+int(b))
        
        
    except EOFError:
        break