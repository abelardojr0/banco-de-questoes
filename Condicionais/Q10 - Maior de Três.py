# Solicita ao usuário que digite três números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

# Verifica qual é o maior número
if numero1 == numero2 and numero2 == numero3:
    print("Os três números são iguais.")
else:
    maior_numero = numero1  # Assume que o primeiro número é o maior
    if numero2 > maior_numero:
        maior_numero = numero2  # Atualiza se o segundo número for maior
    if numero3 > maior_numero:
        maior_numero = numero3  # Atualiza se o terceiro número for maior

    print(f"O maior número entre {numero1}, {numero2} e {numero3} é: {maior_numero}")
