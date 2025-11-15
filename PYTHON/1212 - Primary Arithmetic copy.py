while True:
    a,b = map(str,input().split())
    if a == b and a =='0':
        break

    a = list(reversed([int(x) for x in a]))
    
    b = list(reversed([int(x) for x in b]))

    while len(a)< len(b):
        a.append(0)
    while len(b)< len(a):
        b.append(0)

    mod = 0
    c = 0
    for i in range(len(a)):
        if a[i] + b[i] + mod >= 10:
            mod = 1
            c+=1
        else:
            mod = 0

    if c == 0:
        print('No carry operation.')
    elif c ==1:
        
        print(f'{c} carry operation.')

    else:
        print(f'{c} carry operations.')