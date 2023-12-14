# Definindo uma função lambda que retorna a soma dos números ímpares em uma lista
soma_impares = lambda lista: sum(filter(lambda x: x % 2 != 0, lista))

# Exemplo de uso
# Definindo uma lista de números para encontrar a soma dos ímpares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Chamando a função lambda para encontrar a soma dos números ímpares na lista
resultado = soma_impares(numeros)

# Imprimindo o resultado
print(resultado)
