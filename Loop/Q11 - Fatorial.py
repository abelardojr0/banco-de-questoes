# Solicita ao usuário que digite um número inteiro e positivo
numero = int(input("Digite um número inteiro e positivo: "))

# Verifica se o número é um valor válido
if numero < 0:
    print("Número inválido. Por favor, insira um número inteiro e positivo.")
else:
    # Inicializa o fatorial como 1
    fatorial = 1

    # Calcula o fatorial do número
    for i in range(1, numero + 1):
        fatorial *= i

    # Exibe o resultado
    print(f"O fatorial de {numero} é: {fatorial}")
