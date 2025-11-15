while True:
    try:
        v = []
        n = int(input())
        for i in range(n):
            a = list(map(str,input().split()))
            v.append([a[0],a[1],int(a[2])])

        v.sort(key= lambda x: (x[2],x[1],(x[0])))
        
        for i in range(n):
            print(v[i][0])
    except EOFError:
        break