# Inicializa a variável para armazenar a soma
soma = 0

# Solicita ao usuário que digite 10 números
for i in range(1,11):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

# Exibe a soma dos números digitados
print(f"A soma dos números digitados é: {soma}")
