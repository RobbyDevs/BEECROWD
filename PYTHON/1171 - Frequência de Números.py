N = int(input())

# Leitura dos valores
valores = [] #criando a lista que armazenarah os valores digitados
for i in range(0,N):  #Laco: para cada i no intervalo de 1 e N...
    valor = int(input())    #...ler um valor e salvar em "valor"
    valores.append(valor)   #...adicionar "valor" ao vetor "valores"

# Contagem das frequencias
frequencias = [] #criando uma lista que armazenarah a frequencia de cada valor
for valor in valores:   #laco: para cada valor no vetor "valores"...
    if valor in frequencias:    #condicao: se "valor" estvier contido no vetor "frequencias"
        frequencias[valor] += 1 # o que estiver na posicao "valor" do vetor "frequencias" vai somar 1.
    else:
        frequencias[valor] = 1 # se nao, o que estvier nessa posicao receberah 1

print())

