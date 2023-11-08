# Solicita que o usuário escolha uma cor e armazena o valor na variável 'cor'
cor = int(input("""
          Escolha uma cor:
          1 - Vermelho
          2 - Amarelo
          3 - Verde
"""))

# Verifica o valor da variável 'cor' para determinar qual mensagem deve ser impressa
if cor == 1:
    # Se 'cor' for igual a 1, imprime a mensagem "Pare! Sinal vermelho"
    print("Pare! Sinal vermelho")
elif cor == 2:
    # Se 'cor' for igual a 2, imprime a mensagem "Atenção! Sinal amarelo"
    print("Atenção! Sinal amarelo")
elif cor == 3:
    # Se 'cor' for igual a 3, imprime a mensagem "Acelere! Sinal verde"
    print("Acelere! Sinal verde")
else:
    # Se 'cor' não for igual a 1, 2 ou 3, imprime a mensagem "Opção Inválida"
    print("Opção Inválida")
