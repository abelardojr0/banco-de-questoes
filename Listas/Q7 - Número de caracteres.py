# Dada a lista de palavras
palavras = ['python', 'java', 'c++', 'javascript']

# Cria uma nova lista para armazenar o número de caracteres de cada palavra
num_caracteres = []

# Itera sobre cada palavra na lista e adiciona o número de caracteres à nova lista
for palavra in palavras:
    num_caracteres.append(len(palavra))

# Imprime a lista resultante item por item
for item_atual in num_caracteres:
    print(item_atual)
