# Solicita ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
while True:

    #Inicia a variável resultado como 0
    resultado = 0

    # Exibe o menu de operações
    escolha = int(input("""
          Escolha uma operação:
          1 - Somar
          2 - Subtrair
          3 - Multiplicar
          4 - Dividir
          0 - Sair
"""))
    match escolha:
      case 1:
        resultado = num1 + num2
      case 2:
        resultado = num1 - num2
      case 3:
        resultado = num1 * num2
      case 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
      case 0:
        print("Programa encerrado.")
        break
      case _:
        print("Opção inválida. Por favor, escolha uma operação válida.")
    print(f"O resultado é: {resultado}")
