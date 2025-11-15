for w in range(int(input())):
    
    a,b = input().split()
    
    if b in a[(len(b)-len(a)-1):]:
        print('encaixa')
    else:
        print('nao encaixa')