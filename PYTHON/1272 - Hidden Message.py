for i in range(int(input())):
    
    try:
        v = list(map(str,input().split()))
    except ValueError:
        print()
        continue
        
    for i in range(len(v)):
        print(v[i][0],end='')
    print()