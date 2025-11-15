t = input()
tl = list(t)
r = 0

if "7" in tl:
    for i in range(0,(len(tl))):
        if tl[i] == "7":
            tl[i] = "0"

t = "".join(tl)
a,op,b = list(map(str,t.split()))
a,b = int(a), int(b)
if op == "+":
    r = a+b
elif op == "-":
    r = a-b
elif op == "/" and b!=0:
    r = a/b
elif op == "*":
    r = a*b

rl = list(str(r))

for i in range(0,len(rl)):
    if rl[i] == "7":
        rl[i] = "0"
r = int("".join(rl))

print(r)