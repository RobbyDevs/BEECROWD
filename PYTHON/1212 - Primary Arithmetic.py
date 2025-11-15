while True:
    a,b = map(str,input().split())
    if a == b and a =='0':
        break

    a = list(reversed([int(x) for x in a]))
    
    b = list(reversed([int(x) for x in b]))

    if len(a)>len(b):
        leng = len(b)
    elif len(a) < len(b):

        leng = len(a)
    else:
        leng = len(a)

    mod = 0
    c = 0
    for i in range(leng):
        if a[i] + b[i] + mod >= 10:
            mod = 1
            c+=1

    if c == 0:
        print('No carry operations.')
    elif c ==1:
        
        print(f'{c} carry operation.')

    else:
        print(f'{c} carry operations.')