for w in range(int(input())):
    
    dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    v = input()
    n = int(input())
    
    if n ==0:
        print(v)
    else:
        for i in v:

            print(dic[dic.index(i)-n],end='')
        print()