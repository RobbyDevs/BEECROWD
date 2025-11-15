n = int(input()) # leitura da linha que comportarah o n de casos de testes
v = 0 #declaracao da variavel que armazenara a soma dos numeros de leds
dic = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}

'''declaaracao do dicionario 'dic'

O dicionario eh composto e um indice e um valor.qz

Cada numero de 0 a 9 utiliza um valor fixo de LEDs, usaremos o proprio Indice como o numero em
questao e o valor contido neste indice serah o numero de LEDs que ele utilizah.

Neste problema, iremos realizar uma operacao matematica, entao eh importante saber qual valor do
dicionario serah String e qual serah Integer. O Indice deverah ser do tipo String, pois iremos
compara-lo com o valor digitado na entrada de dados (que tambem serah String) para poder percorrermos
cada um dos caracteres do texto digitado e realizar a consulta no dicionario.

Como iremos somar o valor contido dentro de cada indice (nao o indice em si), logo, este deverah
ser do tipo inteiro.


'''

#   Inicio do programa
for i in range(0,n):    #Repeticao dos numeros de casos de restes (n)
    t = input()    # entrada do valor que serah no formato String
# Strings sao vetores, e vetores possuem indices. Cada caractere da String eh um indice.
    
    #inicio do percurso no texto
    for j in range(0,(len(t))): #para cada j comecando em 0 e indo ate o numero de caracteres em "t"

        v = v + dic[t[j]]   # 'v' vai armazenar o valor dele mesmo + o valor contido no dicionario
                            # no caractere 'j' do texto 't'.
    '''

    Entao V vai receber 0 + dic[t[j]]. Mas o que isso quer dizer?

        dic[t[j]] quer dizer:
            "No dicionario, retornar o valor que estah contido no indice [t[j]]
                O indice [t[j]] eh o indice j do texto 't'.
    Ou seja, o caractere do indice 'j' do texto 't' dentro do dicionario 'dic'.


    ----- Por exemplo:-----------------------------------------

    't' tem como texto "821".

    No primeiro laco, j == 0 e v == 0.

    Entao v = v + o primeiro caractere do texto 't', no caso, "8". Esse "8" eh um indice no dicionario.
    "8" no dicionario corresponde ao valor 7. 
    Logo, estou dizendo para v armazenar v + o valor do dicionario que corresponde ao primeiro indice
    do texto 't', ou seja, o valor 7.

    Logo, v = 0 + 7.
    V == 7

    No segundo laco, j == 1 e v == 7.
    Entao v = v + o segundo caractere do texto 't', no caso, "2". Esse "2" tem como valor o numero 5 no dicionario.

    Logo, v = 7 + 5.
    V == 12

    No terceiro laco, j == 2 e v == 12.
    Entao v = 12 + o valor armazenado no indice "1" do dicionario, ou seja, 2.

    Logo, v = 12 + 2
    v == 14

        Fim do numero de caracteres de 't'.

    '''

    print(f"{v} leds") # imprimir o valor contido em 'v'.
    v=0   # zerar o valor contido em 'v' para reiniciar o proximo caso de teste.

# fim do caso de teste.