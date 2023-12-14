def conta_pares_impares(lista):
    # Inicializa contadores para números pares e ímpares
    pares = 0
    impares = 0
    
    # Itera sobre a lista de números
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return [pares, impares]

# Exemplo de uso
numeros = []
for i in range (10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

quantidade_pares = conta_pares_impares(numeros)[0]
quantidade_impares = conta_pares_impares(numeros)[1]

print(f'Quantidade de números pares: {quantidade_pares}')
print(f'Quantidade de números ímpares: {quantidade_impares}')
