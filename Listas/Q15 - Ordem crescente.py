# Dada a lista de produtos
produtos = [('Mouse', 25.99), ('Teclado', 59.99), ('Mousepad', 15.99), ("Monitor", 600.00), ("Fone de Ouvido", 110.50)]

# Cria uma nova lista apenas com os preços
precos = []
for produto in produtos:
    precos.append(produto[1])

# Ordena a lista de preços em ordem crescente
precos.sort()

# Imprime a lista de preços ordenada
print("Preços dos produtos em ordem crescente:")
for preco in precos:
    print(preco)
