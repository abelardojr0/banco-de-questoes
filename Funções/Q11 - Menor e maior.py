def menor_maior_elemento(lista):
    # Verifica se a lista é vazia
    if not lista:
        return "Lista vazia"

    # Inicializa os valores de menor e maior com o primeiro elemento da lista
    menor  = lista[0]
    maior = lista[0]

    # Itera sobre a lista para encontrar o menor e o maior elemento
    for elemento in lista:
        if elemento < menor:
            menor = elemento
        elif elemento > maior:
            maior = elemento

    # Retorna uma lista contendo o menor e o maior elemento
    return [menor, maior]

# Inicializa uma lista vazia chamada 'numeros'
numeros = []
# Solicita ao usuário que digite cinco números e os adiciona à lista 'numeros'
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Chama a função menor_maior_elemento passando a lista 'numeros' como argumento
# e armazena o resultado nas variáveis 'menor' e 'maior'
menor = menor_maior_elemento(numeros)[0]
maior = menor_maior_elemento(numeros)[1]

# Imprime os resultados
print(f'Menor elemento: {menor}')
print(f'Maior elemento: {maior}')
