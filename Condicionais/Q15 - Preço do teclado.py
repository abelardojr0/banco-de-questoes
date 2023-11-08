# Solicita ao usuário que digite o número de teclados comprados
numero_teclados = int(input("Digite o número de teclados comprados: "))

# Define o preço unitário dos teclados
preco_unitario = 30  # Preço padrão se forem comprados menos de uma dúzia

# Verifica se foram comprados pelo menos uma dúzia
if numero_teclados >= 12:
    preco_unitario = 25  # Preço se forem comprados pelo menos uma dúzia

# Calcula o valor total da compra
valor_total = numero_teclados * preco_unitario

# Exibe o valor total da compra
print(f"O valor total da compra é: R${valor_total:.2f}")
