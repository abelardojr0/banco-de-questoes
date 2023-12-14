def par(numero):
    # Verificando se o resto da divisão por 2 é zero (se é par)
    if numero % 2 == 0:
        return True
    else:
        return False

# Exemplo de uso da função
numero_informado = int(input("Digite um número: "))

# Chamando a função eh_par com o número informado e imprimindo o resultado
if par(numero_informado):
    print(f"{numero_informado} é um número par.")
else:
    print(f"{numero_informado} não é um número par.")
