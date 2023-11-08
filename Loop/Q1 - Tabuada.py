# Solicita ao usuário que digite um número inteiro entre 1 e 10
numero = int(input("Digite um número inteiro entre 1 e 10: "))

# Verifica se o número está dentro do intervalo desejado
if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número fora do intervalo permitido. Por favor, insira um número entre 1 e 10.")
