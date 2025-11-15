txt = input()

txtl = list(txt)

if "7" in txtl:
    for i in range(0,(len(txtl))):
        if txtl[i] == "7":
            txtl[i] = "0"

txtf = "".join(txtl)

a,op,b = list(map(str,txtf.split()))

a,b = int(a),int(b)

if op == "+":
    r = a+b
elif op == "-":
    r = a-b
elif op == "/" and b!= 0:
    r = a/b
elif op == "x":
    r = a*b

rtxt = str(r)
rl = list(rtxt)
if "7" in rl:
    for i in range(0,len(rl)):
        if rl[i] == "7":
            rl[i] = "0"
r = "".join(rl)
print(int(r))
# o resultado esta contendo zeros aa esquerda.
# Remover os zeros aa esquerda e imprimir a saida.