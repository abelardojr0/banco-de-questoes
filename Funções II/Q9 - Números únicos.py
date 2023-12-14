# Lista original de números
numeros = [1, 2, 3, 2, 4, 5, 6, 5, 7, 8, 9, 1]

# Utilizando uma função lambda para filtrar os números únicos na lista
# A expressão lambda verifica quantas vezes um número aparece na lista usando 'numeros.count(x)'
# Retorna True apenas para os números que aparecem uma vez (ou seja, são únicos)
numeros_unicos = list(filter(lambda x: numeros.count(x) == 1, numeros))

# Exibindo a lista de números únicos
print(numeros_unicos)
