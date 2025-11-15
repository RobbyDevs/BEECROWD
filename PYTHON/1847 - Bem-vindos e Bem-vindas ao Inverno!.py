a,b,c = map(int,input().split())

t = ":)"

if b>a and c<=b:
    t = ":("
elif b>a and c>=b and (c-b)<(b-a):
    t = ":("

elif a>b and c<=b and(b-c)>=(a-b):
    t = ":("
elif a == b and c<=b:
    t = ":("

print(t)