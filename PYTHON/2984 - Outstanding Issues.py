v = [str(x) for x in input()]

va = []

for i in v:
    if i == '(':
        va.append(i)
    else:
        
        if len(va)>0:
            va.pop()
            

l = len(va)
if l >0:
    print(f'Ainda temos {l} assunto(s) pendente(s)!')
else:
    print(f'Partiu RU!')