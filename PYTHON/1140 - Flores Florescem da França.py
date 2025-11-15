while True:
    txt = input()
    if txt == "*":
        break
    else:
        c = "Y"
        txtmin = txt.lower()
        palavras = list(map(str,txtmin.split()))
        for i in range(0,(len(palavras))):
            if palavras[0][0] != palavras[i][0]:
                c = "N"
                break
        print(c)