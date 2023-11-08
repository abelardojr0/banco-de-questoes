# Inicializa a variável para armazenar o maior número
maior_numero = 0

# Solicita ao usuário que digite 10 números inteiros
for i in range(1,11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    
    # Verifica se o número é maior do que o maior número atual
    if numero > maior_numero:
        maior_numero = numero

# Exibe o maior número digitado
print(f"O maior número digitado é: {maior_numero}")
