# Inicializa as variáveis para contar números pares e ímpares
quantidade_pares = 0
quantidade_impares = 0

# Solicita ao usuário que insira 10 números inteiros
for i in range(1,11):
    numero = int(input(f"Digite o {i}º número inteiro: "))

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

# Exibe a quantidade de números pares e ímpares
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
