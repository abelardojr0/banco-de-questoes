def verifica_primo(numero):
    # Verifica se o número é menor que 2, pois números menores que 2 não são primos
    if numero < 2:
        return False
    
    # Verifica se o número é divisível por algum número de 2 até a raiz quadrada do próprio número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    # Se não foi encontrado nenhum divisor, o número é primo
    return True

# Exemplo de uso
numero = int(input("Digite um número: "))
resultado = verifica_primo(numero)

if resultado:
    print(f'{numero} é primo.')
else:
    print(f'{numero} não é primo.')
