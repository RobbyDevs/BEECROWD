while True:
    try:
        n = int(input())
        v = []
        
        while True:
            a = list(map(str,input().split()))
            if '0' in a:
                break
            a = a[1]
            v.append(a)
            
        v.sort(key= lambda x: int(x))
        
        for i in v:
            print(f'Package {i}')
        print()
        
    except EOFError:
        break
    