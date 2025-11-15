while True:
    try:
        v = []
        for i in range(int(input())):
            v.append(input().split())
            
        for i in range(len(v)):
            v[i][1] = int(v[i][1])
        
        v.sort(key= lambda x: x[1])

        for i in range(len(v)-1):
            print(v[i][0],end=' ')
        print(v[len(v)-1][0])
        
        
    except EOFError:
        break
    
