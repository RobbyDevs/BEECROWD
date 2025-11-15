for w in range(int(input())):
    
    v = input()
    
    if len(v)==20:
        if v[0:2] == 'RA':
            print(int(v[2:]))
        else:
            print('INVALID DATA')
    else:
            print('INVALID DATA')
            
