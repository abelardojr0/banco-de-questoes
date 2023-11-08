# Solicita que o usuário digite um número e armazena o valor na variável 'numero'
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 2, ou seja, se o resto da divisão por 2 é igual a zero
if numero % 2 == 0:
    # Se a condição for verdadeira, imprime uma mensagem informando que o número é par
    print(f"O {numero} é par")

# Caso a condição acima seja falsa (o resto da divisão por 2 não é zero), significa que o número é ímpar
else:
    # Nesse caso, imprime uma mensagem informando que o número é ímpar
    print(f"O {numero} é ímpar")
