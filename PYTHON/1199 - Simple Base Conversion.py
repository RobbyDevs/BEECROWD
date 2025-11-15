while True:
    v = input()
    if v[0]=='-':
        break

    if v[0:2] == '0x':
        print(int(v,16))
    else:
        hexa = hex(int(v))
        print(f'{hexa[0:2]}{(hexa[2:]).upper()}')