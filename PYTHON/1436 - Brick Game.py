for w in range(int(input())):
    
    v = list(map(int,input().split()))
    
    n = v[0]
    v.pop(0)
    
    v.sort()
    
    print(f'Case {w+1}: {v[n//2]}')