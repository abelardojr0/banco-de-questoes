# Solicita que o usuário escolha um dia da semana e armazena o valor na variável 'dia'
dia = int(input("""
          Escolha o dia da semana
          1 - Domingo
          2 - Segunda-Feira
          3 - Terça-Feira
          4 - Quarta-Feira
          5 - Quinta-Feira
          6 - Sexta-Feira
          7 - Sábado
"""))

# O bloco "match" é usado para comparar o valor da variável 'dia' com várias opções
match dia:
  case 1:
    # Se 'dia' for igual a 1, imprime a mensagem correspondente a Domingo
    print("Você escolhe o Domingo")
  case 2:
    # Se 'dia' for igual a 2, imprime a mensagem correspondente a Segunda-Feira
    print("Você escolhe a Segunda-Feira")
  case 3:
    # Se 'dia' for igual a 3, imprime a mensagem correspondente a Terça-Feira
    print("Você escolhe a Terça-Feira")
  case 4:
    # Se 'dia' for igual a 4, imprime a mensagem correspondente a Quarta-Feira
    print("Você escolhe a Quarta-Feira")
  case 5:
    # Se 'dia' for igual a 5, imprime a mensagem correspondente a Quinta-Feira
    print("Você escolhe a Quinta-Feira")
  case 6:
    # Se 'dia' for igual a 6, imprime a mensagem correspondente a Sexta-Feira
    print("Você escolhe a Sexta-Feira")
  case 7:
    # Se 'dia' for igual a 7, imprime a mensagem correspondente a Sábado
    print("Você escolhe a Sábado")
  case _:
    # Se 'dia' não corresponder a nenhuma das opções anteriores, imprime "Opção inválida"
    print("Opção inválida")
