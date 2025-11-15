for w in range(int(input())):
    
    v = sorted(set(list(map(str,input().split()))))
    print(' '.join(v))