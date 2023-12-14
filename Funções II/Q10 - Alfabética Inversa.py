# Lista original de strings
palavras = ["banana", "abacaxi", "laranja", "uva", "abacate"]

# Utilizando uma função lambda para ordenar a lista em ordem alfabética inversa
palavras_ordenadas = sorted(palavras, key=lambda x: x, reverse=True)

# Exibindo a lista ordenada
print(palavras_ordenadas)
