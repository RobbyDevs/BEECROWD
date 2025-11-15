while True:
    try:
        n = int(input())
        
        for i in range(1,n+1,2):
            print(' '*((n-i)//2),'*'*i,sep='')
        
        print(' '*(n//2),'*',sep='')
        print(' '* ((n//2)-1),'***',sep='')
        
        print()
    except EOFError:
        break