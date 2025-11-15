a =  int(input())
b = int(input())
c = int(input())
d  =int(input())
e = int(input())

p=im=pos=neg = 0
v = [a,b,c,d,e]

for i in v:
    if i % 2 == 0:
        p +=1
    else:
        im +=1
    if i > 0:
        pos +=1
    elif i < 0:
        neg +=1
        
print(f'{p} valor(es) par(es)')
print(f'{im} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
