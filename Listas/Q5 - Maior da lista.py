# Cria uma lista vazia chamada "numeros"
numeros = []

# Pede ao usuário para inserir 5 números usando um loop for
#Usamos de 1 a 6 para ele mostrar na tela de 1 a 5
for i in range(1, 6):
    # Utiliza a função input() para obter um número do usuário e o converte para o tipo float
    numero_inserido = float(input(f"Insira o {i}º número: "))
    
    # Adiciona o número à lista "numeros"
    numeros.append(numero_inserido)

# Inicializa a variável "maior_numero" com o primeiro número da lista
maior_numero = numeros[0]

# Percorre a lista para encontrar o maior número
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

# Imprime o resultado 
print(f"O maior número na lista é: {maior_numero}")
