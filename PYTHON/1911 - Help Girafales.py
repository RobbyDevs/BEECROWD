while True:
    
    
    n = int(input())
    if n == 0:
        break
    
    dic = {}
    for i in range(n):
        a,b = map(str,input().split())
        dic[a] = b
    s = 0
    for i in range(int(input())):
        a,b = map(str,input().split())
        c = 0
        
        
        for j in range(len(dic[a])):
            if c >1:
                break
            if b[j] != dic[a][j]:
                c+=1
        if c>1:
            s+=1
    print(s)

