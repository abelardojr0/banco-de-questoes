# Definindo a função soma_numeros
def soma_numeros(numero1, numero2):
    # Calculando a soma dos dois números
    soma = numero1 + numero2
    # Retornando o resultado da soma
    return soma

# Exemplo de uso da função
# Solicitando ao usuário que insira o primeiro número
num1 = float(input("Digite o primeiro número: "))
# Solicitando ao usuário que insira o segundo número
num2 = float(input("Digite o segundo número: "))

# Chamando a função soma_numeros com os números fornecidos pelo usuário
resultado = soma_numeros(num1, num2)
# Imprimindo o resultado da soma
print(f"A soma de {num1} e {num2} é: {resultado}")
