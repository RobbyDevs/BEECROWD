while True:
    v = input()
    if v == '0':
        break
    else:
        v = list(map(int,v.split()))
        n = v[0]
        v.remove(v[0])
        c = 0
        
        for i in range(n):
            while v[i] != i+1:
                aux = v[i] -1
                v[i],v[aux] = v[aux],v[i]
                c+=1
            

    if c == 0:
        print('Carlos')
        
    elif c %2 == 0:
        print("Carlos")
    else:
        print('Marcelo')