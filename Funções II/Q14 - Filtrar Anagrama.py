# Função para verificar se duas palavras são anagramas
eh_anagrama = lambda palavra1, palavra2: sorted(palavra1) == sorted(palavra2)

# Palavra específica para encontrar anagramas
palavra_referencia = "listen"

# Lista original de palavras
palavras = ["silent", "enlist", "orchestra", "dog", "tinsel", "inlets"]

# Utilizando filter e uma função lambda para filtrar anagramas da palavra de referência
anagramas = list(filter(lambda x: eh_anagrama(x, palavra_referencia), palavras))

# Exibindo a lista resultante
print(anagramas)
