vn = '1234567890.'
vnn = '1234567890'
va = ''.join([str(x) for x in input() if x in vn])
vb = ''.join([str(x) for x in input() if x in vn])


cpf = ''.join([str(x) for x in va if x in vnn])[:11]

print()
print(cpf)
print(va)
print(int(vb)+111.23)
