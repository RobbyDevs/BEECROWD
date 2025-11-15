dic = {"W":1,"H":1/2,"Q":1/4,"E":1/8,"S":1/16,"T":1/32,"X":1/64}
while True:
    
    s = 0
    r = 0

    v = list(map(str,input().split("/")))
    
    if v[0] == '*':break
    
    for i in range(len(v)):
        s = 0
        for j in range(len(v[i])):
           s+= dic[v[i][j]]
        if s >=0.99999 and s<=1:
            r+=1
    print(r)