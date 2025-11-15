while True:
    try:
        v = input()
        
        if v[2]=='L':
            print('Esse eh o meu lugar')
        else:
            print('Oi, Leonard')
    except EOFError:
        break