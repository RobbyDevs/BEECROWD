nn = int(input())
for w in range(nn):
    m,n = map(int,input().split())
    
    dic = {}
    
    for i in range(m):
        a = input()
        b = input()
        
        dic[a] = b
        
    for i in range(n):
        a = input().split()
        
        for j in range(len(a)):
            try:
                print(dic[a[j]],end='')
                if j<len(a)-1:
                    print(end=' ')
            except:
                print(a[j],end='')
                if j<len(a)-1:
                    print(end=' ')
        
        
        print()
    print()
