# Solicita ao usuário que digite um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Verifica se o número é divisível por 3 e por 5 ao mesmo tempo
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"O número {numero} é divisível por 3 e por 5 ao mesmo tempo.")
    else:
        print(f"O número {numero} não é divisível por 3 e por 5 ao mesmo tempo.")
