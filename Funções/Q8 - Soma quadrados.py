def soma_quadrados(a, b):
    resultado = a**2 + b**2
    return resultado

# Exemplo de uso
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = soma_quadrados(numero1, numero2)

print(f'A soma dos quadrados de {numero1} e {numero2} é: {resultado}')
