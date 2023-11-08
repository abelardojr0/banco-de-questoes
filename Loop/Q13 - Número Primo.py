# Solicita ao usuário que insira um número inteiro e positivo
numero = int(input("Digite um número inteiro e positivo: "))

# Verifica se o número é maior que 1
if numero > 1:
    # Inicializa uma variável para contar os divisores
    divisores = 0

    # Percorre os números de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        # Verifica se o número é divisível por 'i'
        if numero % i == 0:
            divisores += 1
            break  # Se for divisível, não é primo, então saímos do loop

    # Se não houver divisores além de 1 e o próprio número, é primo
    if divisores == 0:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
else:
    print("Número inválido. Por favor, insira um número inteiro e positivo maior que 1.")
