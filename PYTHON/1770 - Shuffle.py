while True:
    try:
        m,k = map(int,input().split())

        v = list(map(int,input().split()))
        vp = list(map(int,input().split()))

        dic = {}
        s = set()
        for i in range(m):
            dic[i+1]=v[i]

        ans = 0

        for i in range(k):
            if len(s)>=m:
                print(ans)
                break
            else:
                s.add(vp[i])
                ans +=dic[vp[i]]
        else:
            print(-1)
            
    except EOFError:
        break
    
