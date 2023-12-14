# Lista original de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Utilizando uma função lambda para filtrar os números pares e calcular o quadrado de cada um
quadrados_numeros_pares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))

# Exibindo a lista de quadrados dos números pares
print(quadrados_numeros_pares)
