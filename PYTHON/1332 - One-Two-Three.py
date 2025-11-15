v = ['one','two']
for w in range(int(input())):
     
    a = input()
     
    if len(a) == 5:
         print(3)
         continue
    ind = 0
    for i in range(2):
        c = 0
        for j in range(3):
            if a[j]!=v[i][j]:
                c+=1
        
        if c <= 1:
            print(i+1)
            continue
     
     