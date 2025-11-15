while True:
    n = int(input())
    if n == 0:
        break
    for w in range(n):
        
        v = list(map(int,input().split()))
        s = 'ABCDE'
        va = []
        for w in range(5):
            if v[w] <= 127:
                if len(va) == 0:
                    va.append(w)
                else:
                    print('*')
                    break
        else:
            if len(va) == 1:
                print(s[va[0]])
            else:
                print('*')
