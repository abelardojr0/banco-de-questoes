# Solicita que o usuário digite seu ano de nascimento e armazena o valor na variável 'nascimento'
nascimento = int(input("Digite seu ano de nascimento: "))

# Calcula a idade subtraindo o ano de nascimento do ano atual (2023)
idade = 2023 - nascimento

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    # Se a condição for verdadeira, imprime uma mensagem informando que a pessoa é maior de idade
    print(f"Você já é maior de idade, pois já tem {idade} anos")

# Caso a condição acima seja falsa (a idade é menor que 18), significa que a pessoa é menor de idade
else:
    # Nesse caso, imprime uma mensagem informando que a pessoa ainda não atingiu a maioridade
    print(f"Você ainda não é maior de idade, pois tem apenas {idade} anos")
