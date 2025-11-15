vn = '1234567890'
vnp = '.1234567890'


va = input()

vb = input()

cpf = ''.join([str(x) for x in va if x in vn][:11]) # CPF = OK


extra = (''.join([str(x) for x in va if x in vnp])[11:])
#print(extra)

extra = int((float(extra)*100))/100

val = (''.join([str(x) for x in vb if x in vnp]))
val =  int((float(val)*100))/100
print(f'cpf {cpf}')
print(f'{(val+extra):.2f}')