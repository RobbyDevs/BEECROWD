import sys

read = sys.stdin.readline
write = sys.stdout.write

for w in range(int(read())):
    n = int(read())
    vf = [0] * 211
    
    for h in map(int, read().split()):
        vf[h - 20] += 1
    
    first = True
    for i in range(211):
        if vf[i]:
            val = str(i + 20)
            if first:
                first = False
            else:
                write(' ')
            write((val + ' ') * vf[i])
    
    write('\n')
