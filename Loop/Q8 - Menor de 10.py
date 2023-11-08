# Inicializa a variável para armazenar o menor número 
#float("inf") é o infinito, ou seja não existe um valor mais alto que ele
menor_numero = float("inf")

# Solicita ao usuário que digite 10 números inteiros
for i in range(1,11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    
    # Verifica se o número é menor do que o menor número atual
    if numero < menor_numero:
        menor_numero = numero

# Exibe o menor número digitado
print(f"O menor número digitado é: {menor_numero}")
