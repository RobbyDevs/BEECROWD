import sys

# Inicializando variáveis
ultimo_numero_valido = None
invalido_encontrado = False

# Leitura da entrada até o EOF (final do arquivo)
for linha in sys.stdin:
    # Convertendo a linha em um número inteiro
    numero = int(linha.strip())
    
    if ultimo_numero_valido is None:
        # O primeiro número sempre será válido
        ultimo_numero_valido = numero
    elif not invalido_encontrado:
        # Se ainda não encontramos o número inválido
        if numero > ultimo_numero_valido:
            ultimo_numero_valido = numero  # Atualiza o último número válido
        else:
            invalido_encontrado = True     # Identifica o primeiro número inválido

# Ao final, imprime o próximo número válido que deveria ser gerado
print(ultimo_numero_valido + 1)
