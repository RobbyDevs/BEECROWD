import sys

ler = sys.stdin.readline

val = (ler().split())[0]

print(val)
while int(val)>9:
    
    ult = int(val[-1])
    
    val = (int(val)//10)*10
    val = (val*3//10)+ult
    print(val)
    val = str(val)