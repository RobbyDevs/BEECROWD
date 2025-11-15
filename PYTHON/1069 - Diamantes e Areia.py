n = int(input())

for i in range(0,n):
    txt = list(input())
    d = 0
    isclean = False
    l = len(txt)
    while True:
        if isclean == True:
            break
        else:
            isclean = True
            for x in range(0,l):
                deleted = False
                if txt[x] == "<":
                    for y in range(x,l):
                        if txt[y] == ">":
                            d+=1
                            del(txt[y])
                            del(txt[x])
                            l = l-2
                            isclean = False
                            deleted = True
                            break
                if deleted == True:
                    break
                        


    print(d)