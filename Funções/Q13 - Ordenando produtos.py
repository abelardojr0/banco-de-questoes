def ordena_produtos(lista_produtos):
    # A função recebe uma lista de dicionários representando produtos
    
    # Ordena a lista de produtos com base no preço
    # A função sorted é usada para ordenar a lista de produtos
    # A chave de ordenação (key) é definida usando uma expressão lambda para extrair o valor do preço de cada produto
    # A função get é usada para acessar o valor associado à chave 'preco', com 0 como valor padrão
    lista_ordenada = sorted(lista_produtos, key=lambda x: x.get('preco', 0))

    # Retorna a lista de produtos ordenada pelo preço em ordem crescente
    return lista_ordenada

# Exemplo de uso
# Criamos uma lista de produtos, onde cada produto é representado por um dicionário
produtos = [
    {'nome': 'Produto A', 'preco': 20.0},
    {'nome': 'Produto B', 'preco': 15.0},
    {'nome': 'Produto C', 'preco': 25.0}
]

# Chama a função ordena_produtos passando a lista de produtos como argumento
produtos_ordenados = ordena_produtos(produtos)

# Imprime a lista de produtos ordenada
# Iteramos sobre a lista ordenada e imprimimos os detalhes de cada produto
for produto in produtos_ordenados:
    print(f"Nome: {produto['nome']}, Preço: {produto['preco']}")
