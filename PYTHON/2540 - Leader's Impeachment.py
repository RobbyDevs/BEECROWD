while True:
    try:
        
        n = int(input())
        
        if sum(list(map(int,input().split())))/n >= 2/3:
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break