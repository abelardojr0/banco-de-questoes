# Solicita que o usuário digite o primeiro número e armazena o valor na variável 'numero1'
numero1 = int(input("Digite o primeiro número: "))

# Solicita que o usuário digite o segundo número e armazena o valor na variável 'numero2'
numero2 = int(input("Digite o segundo número: "))

# Verifica se 'numero1' é maior que 'numero2'
if numero1 > numero2:
    # Se a condição for verdadeira, imprime uma mensagem informando que 'numero1' é maior que 'numero2'
    print(f"O {numero1} é maior que o {numero2}")

# Caso a condição acima seja falsa, verifica se 'numero2' é maior que 'numero1'
elif numero2 > numero1:
    # Se essa condição for verdadeira, imprime uma mensagem informando que 'numero2' é maior que 'numero1'
    print(f"O {numero2} é maior que o {numero1}")

# Se ambas as condições acima forem falsas, significa que 'numero1' e 'numero2' são iguais
else:
    # Nesse caso, imprime uma mensagem informando que os números são iguais e exibe o valor dos números
    print(f"Os números são iguais, número digitado: {numero1}")
