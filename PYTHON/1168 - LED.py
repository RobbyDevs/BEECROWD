n = int(input()) # leitura da linha que comportarah o n de casos de testes
v = 0 #declaracao da variavel que armazenara a soma dos numeros de leds
dic = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}

'''declaaracao do dicionario 'dic'

Neste problema, iremos realizar uma operacao matematica, entao eh importante saber qual valor do
dicionario serah String e qual serah Integer.

Como iremos somar o valor contido dentro de cada indice (nao o indice em si), logo, este serah inteiro.



'''
for i in range(0,n):
    t = input()
    for j in range(0,(len(t))):
        v = v + dic[t[j]]
    print(f"{v} leds")
    v=0