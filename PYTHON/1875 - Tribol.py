for w in range(int(input())):
    r = g = b = 0

    for n in range(int(input())):
        fez, tomou = input().split()

        if fez == 'R':
            if tomou == 'G':
                r += 2
            else:
                r += 1
        elif fez == 'G':
            if tomou == 'B':
                g += 2
            else:
                g += 1
        else:
            if tomou == 'R':
                b += 2
            else:
                b += 1

    #print(r, g, b)

    if r == g and g == b: 
        print('trempate')
    elif r > g and r > b:
        print('red')
    elif g > r and g > b:
        print('green')
    elif b > r and b > g:
        print('blue')
    else:
        print('empate')
