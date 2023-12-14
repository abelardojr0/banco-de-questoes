def soma_intervalo(inicio, final):
    # Inicializa o contador de soma
    resultado = 0
    
    # Itera sobre os números no intervalo e adiciona ao resultado
    for num in range(inicio, final + 1):
        resultado += num
    
    return resultado

# Exemplo de uso
comeco = int(input("Digite o começo da contagem: "))
fim = int(input("Digite o fim da contagem: "))
if comeco < fim:
  resultado = soma_intervalo(comeco, fim)
  print(f'A soma dos números no intervalo [{comeco}, {fim}] é: {resultado}')
else:
   print("Você tem que digitar um início menor que o fim")


