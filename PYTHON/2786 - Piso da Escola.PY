l = int(input())
c = int(input())

def t1(l,c):
    return((l*c)+(l-1)*(c-1))



def t2(l,c):
    return((2*(c-1))+(2*(l-1)))
print(t1(l,c))
print(t2(l,c))