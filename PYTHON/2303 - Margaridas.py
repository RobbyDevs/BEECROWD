l,c,m,n = map(int,input().split())
ma= []
for i in range(l):
    ma.append(list(map(int,input().split())))
    
s = 0
ans = 0
for i in range(0,l,m):
    for j in range(0,c,n):
        s = 0
        for x in range(i,i+m):
            for y in range(j,j+n):
                s+=ma[x][y]
        
        if s>ans:
            ans = s
        
        
print(ans)
    

