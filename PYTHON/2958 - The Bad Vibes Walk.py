n,m = map(int,input().split())

v = []

for i in range(n):
    a = list(map(str,input().split()))
    
    for j in a:
        v.append([int(j[0]),j[1]])

v.sort(key= lambda x: (-ord(x[1]),-x[0]))

for i in v:
    print(''.join([str(i[0]),i[1]]))