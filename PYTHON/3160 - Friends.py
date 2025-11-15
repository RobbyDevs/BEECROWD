v = input().split()
vn = input().split()
s = input()

if s == 'nao':
    v.extend(vn)
    print(' '.join(v))
else:
    result = []
    for i in v:
        if i == s:
            result.extend(vn)
            result.append(i)
        else:
            result.append(i)
    print(' '.join(result))
