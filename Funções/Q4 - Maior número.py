def maior_elemento(lista):
    # Verificando se a lista não está vazia
    if not lista:
        return None  # Retorna None se a lista estiver vazia

    # Encontrando o maior elemento na lista usando a função max()
    maior = max(lista)
    return maior

# Exemplo de uso da função
numeros = [17, 42, 8, 93, 11]

# Chamando a função maior_elemento com a lista de números
resultado_maior = maior_elemento(numeros)

# Imprimindo o resultado do maior elemento na lista
print(f"O maior elemento na lista é: {resultado_maior}")
