# Inicializa uma lista vazia para armazenar as palavras
palavras = []

# Solicita ao usuário para inserir palavras até que "sair" seja digitado
while True:
    palavra = str(input("Digite uma palavra (ou 'sair' para encerrar): "))
    
    # Verifica se o usuário deseja sair
    if palavra.lower() == 'sair':
        break
    
    # Adiciona a palavra à lista
    palavras.append(palavra)

# Verifica se há palavras na lista antes de tentar encontrar a maior palavra
if palavras:
    # Inicializa a variável "maior_palavra" com a primeira palavra da lista
    maior_palavra = palavras[0]
    
    # Percorre a lista para encontrar a maior palavra
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    
    # Imprime a maior palavra
    print(f"A maior palavra digitada foi: {maior_palavra}")
else:
    print("Nenhuma palavra foi digitada.")
