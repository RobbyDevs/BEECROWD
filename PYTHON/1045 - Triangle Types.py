v = list(map(float,input().split()))

v.sort(reverse=True)

a,b,c = map(float,v)


if(a>=b+c):
    print("NAO FORMA TRIANGULO")
    
else:
    if((a*a) == (b*b)+(c*c)):
        print("TRIANGULO RETANGULO")
        
    if((a*a) > (b*b)+(c*c)):
        print("TRIANGULO OBTUSANGULO")
        
    if((a*a) < (b*b)+(c*c)):
        print("TRIANGULO ACUTANGULO")
        
    if(a==b and b == c):
        print("TRIANGULO EQUILATERO")
        
    if((a==b and c != a)or (b == c and a !=b)):
        print("TRIANGULO ISOSCELES")