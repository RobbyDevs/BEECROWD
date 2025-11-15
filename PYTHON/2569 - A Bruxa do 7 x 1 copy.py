a, op, b = map(str,input().split())

"""
casos

7 em a e ou em b e ou em r.
7 em 
"""


if op == "+":
    r = int(a) + int(b)
elif op == "-":
    r = int(a) - int(b)
elif op == "/":
    r = int(a) / int(b)
elif op == "*":
    r = int(a) * int(b)

if "7" in a or "7" in b:
    a
else:
    if op == "+":
        r = int(a) + int(b)
    elif op == "-":
        r = int(a) - int(b)
    elif op == "/":
        r = int(a) / int(b)
    elif op == "*":
        r = int(a) * int(b)

la,lb,lr = list(a),list(b),list(str(r))

maisl = max(list((len(la),len(lb),len(lr))))
# maisl == o tamanho do vetor mais longo. Seja ele o termo 1, o 2 ou o resultado
