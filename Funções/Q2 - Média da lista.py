def media_lista(lista):
    # Verificando se a lista não está vazia
    if not lista:
        return "Lista vazia"  # Retorna None se a lista estiver vazia

    # Calculando a média dos valores na lista
    media = sum(lista) / len(lista)
    return media

# Exemplo de uso da função
valores = [4, 7, 10, 13, 5]

# Chamando a função media_lista com a lista de valores
resultado_media = media_lista(valores)

# Imprimindo o resultado da média, formatado com duas casas decimais
print(f"A média dos valores na lista é: {resultado_media:.2f}")
