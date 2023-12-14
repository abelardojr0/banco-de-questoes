# Utilizando uma expressão lambda para encontrar os números divisíveis por 3 no intervalo de 1 a 100
divisiveis_por_3 = list(filter(lambda x: x % 3 == 0, range(1, 101)))

# Exibindo a lista de números divisíveis por 3
print(divisiveis_por_3)
