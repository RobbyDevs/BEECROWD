list = [chr(x) for x in range(0,127)]
txtl = []
alfab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0,(int(input()))):
    txt = input()
    
    for x in range(0,(len(txt))):
        if txt[x] in alfab:
            txtl.append(list)

            print(list)
    
print(txtl)