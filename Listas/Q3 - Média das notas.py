# Dada a lista de notas
notas = [7.5, 8.0, 9.5, 6.0, 8.5]

# Inicializa a variável soma
soma = 0

# Utiliza um loop for para somar todas as notas
for nota in notas:
    soma += nota

# Calcula a média dividindo a soma pelo número de elementos na lista
media = soma / len(notas)

# Imprime o resultado
print(f"Média das notas: {media}")
