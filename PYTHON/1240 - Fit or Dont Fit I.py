for w in range(int(input())):
    
    a,b = map(str,input().split())
    
    if b in a[(len(a)-len(b)):]:
        print('encaixa')
    else:
        print('nao encaixa')