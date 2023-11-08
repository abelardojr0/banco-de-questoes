# Solicita que o usuário digite um número e armazena o valor na variável 'numero'
numero = int(input("Digite um número: "))

# Verifica se 'numero' é maior que 0 (positivo)
if numero > 0:
    # Se a condição for verdadeira, imprime uma mensagem informando que 'numero' é positivo
    print(f"O {numero} é positivo")

# Caso a condição acima seja falsa, verifica se 'numero' é menor que 0 (negativo)
elif numero < 0:
    # Se essa condição for verdadeira, imprime uma mensagem informando que 'numero' é negativo
    print(f"O {numero} é negativo")

# Se ambas as condições acima forem falsas, significa que 'numero' é igual a 0
else:
    # Nesse caso, imprime uma mensagem informando que 'numero' é neutro (igual a zero)
    print(f"O {numero} é neutro")
