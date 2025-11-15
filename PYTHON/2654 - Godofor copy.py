v = []
vb = []
vc = []
vd = []
ma = ''
mb = 0
mc = 0
md = 100

for w in range(int(input())):
    a, b, c, d = map(str, input().split())
    b = int(b)
    c = int(c)
    d = int(d)
    if b > mb:
        mb = b
        ma = a
    if c > mc:
        mc = c
    if d < md:
        md = d
    v.append([a, [b, c, d]])

r = ''

for i in v:
    if i[1][0] == mb:
        vb.append(i)

if len(vb) == 1:
    r = vb[0][0]
else:
    for i in vb:
        if i[1][1] == mc:
            vc.append(i)
    if len(vc) == 1:
        r = vc[0][0]
    elif len(vc) == 0:
        ma = vb[0][0]
        for i in vb:
            if i[0] < ma:
                ma = i[0]
        r = ma
    else:
        for i in vc:
            if i[1][2] == md:
                vd.append(i)
        if len(vd) == 1:
            r = vd[0][0]
        elif len(vd) == 0:
            ma = vc[0][0]
            for i in vc:
                if i[0] < ma:
                    ma = i[0]
            r = ma
        else:
            ma = vd[0][0]
            for i in vd:
                if i[0] < ma:
                    ma = i[0]
            r = ma

print(r)
