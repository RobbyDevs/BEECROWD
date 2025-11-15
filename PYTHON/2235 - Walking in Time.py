v = list(map(int,input().split()))

if len(list(set(v))) < 3:
    print('S')


else:
    if sum(v) - max(v) == sum(v)/2:
        print('S')
    else:
        print('N')