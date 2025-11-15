while True:

    try:
        m = []
        n,y = map(int,input().split())
        c = 0
        for t in range(n):
            v = input().split()
            va = []
            for i in range(len(v)):
                va.append(v[i][0])

            m.append(''.join(va))

        ma = set(m)
        
        print(len(m)- len(ma))

    except EOFError:
        break