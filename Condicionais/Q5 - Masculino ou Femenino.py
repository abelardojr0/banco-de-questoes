# Solicita que o usuário digite o sexo e armazena o valor na variável 'sexo'
sexo = str(input("""
                 Digite o seu sexo:
                  F - Feminino
                  M - Masculino
                 """)).upper().strip()

# Converte a entrada do usuário para letras maiúsculas (usando .upper()) e remove espaços extras (usando .strip())

# Verifica se 'sexo' é igual a "M" (masculino)
if sexo == "M":
    # Se a condição for verdadeira, imprime uma mensagem informando que o sexo escolhido é Masculino
    print("Sexo escolhido: M - Masculino")

# Caso a condição acima seja falsa, verifica se 'sexo' é igual a "F" (feminino)
elif sexo == "F":
    # Se essa condição for verdadeira, imprime uma mensagem informando que o sexo escolhido é Feminino
    print("Sexo escolhido: F - Feminino")

# Se ambas as condições acima forem falsas, significa que a entrada do usuário não é nem "M" nem "F"
else:
    # Nesse caso, imprime uma mensagem informando que o sexo é inválido
    print("Sexo inválido")
