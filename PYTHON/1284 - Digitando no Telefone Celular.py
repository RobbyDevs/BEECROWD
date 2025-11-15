import sys
input = sys.stdin.readline


def dfs(nodo,contagem):
    global ans
    print("tamanho:",len(nodo),">>",nodo)
    print()
    if len(nodo) > 1:
        contagem +=1
        print("Adicionando +1, nova contagem:",contagem)
        
    for c,v in nodo.items():
        if c == "#":
            ans.append(contagem)
            return
        
        else:
            dfs(v,contagem)
            
        # AJUSTAR A PASSADA PELOS NODOS E CONTAGEM DE CARACTERES QUE PRECISAM SER DIGITADOS
        
    return
    
    
    
while True:
    
    n = input()
    #EOF EXCPT
    if n == "":
        break


    else:
        global ans
        ans = []
        
        trie = {}
        n = int(n)
        palavras = []
        for i in range(n):
            palavra = input()
            palavras.append(palavra)
            nodo = trie
            
            
            for letra in palavra:
                
                if letra != "\n":
                    #print(nodo,letra)
                    if letra not in nodo:
                        nodo[letra] = {}
                
                    nodo = nodo[letra]
            
            nodo["#"] = "#" 
            
            
        #print(trie)
        #print()
        if len(trie) <= 1:
            contagem = 1
        else:
            contagem = 0
            
        dfs(trie,contagem)
        print(ans)
        print(f"{(abs(sum(ans))/n):.2f}")

#{'h': {'e': {'l': {'l': {'o': {'#': '#'}, '#': '#'}}, 'a': {'v': {'e': {'n': {'#': '#'}}}}}}, 'g': {'o': {'o': {'d': {'b': {'y': {'e': {'#': '#'}}}}}}}}
#{'h': {'e': {'l': {'l': {'o': {'#': '#'}, '#': '#'}}, 'a': {'v': {'e': {'n': {'#': '#'}}}}}}, 'g': {'o': {'o': {'d': {'b': {'y': {'e': {'#': '#'}}}}}}}}