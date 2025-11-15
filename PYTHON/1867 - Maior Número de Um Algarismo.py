while True:
    m,n = map(list,input().split())
    if m[0] == "0" and n[0] == "0":
        break

    else:
        
        while len(m)>1 or len(n)>1:
            m = [int(x) for x in m]
            n = [int(x) for x in n]

            m = list(str(sum(m)))
            n = list(str(sum(n)))
        if int(m[0]) > int(n[0]):
            print(1)
        elif int(m[0]) < int(n[0]):
            print(2)
        else:
            print(0)