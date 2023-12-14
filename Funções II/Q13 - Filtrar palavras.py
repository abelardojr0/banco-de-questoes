# Lista original de palavras
palavras = ["python", "programação", "linguagem", "oi", "func", "list"]

# Utilizando filter com uma função lambda para filtrar palavras com mais de 5 caracteres
palavras_mais_longas = list(filter(lambda x: len(x) > 5, palavras))

# Exibindo a lista resultante
print(palavras_mais_longas)
