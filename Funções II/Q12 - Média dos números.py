# Definindo uma função lambda que retorna a média aritmética de uma lista de números
media_aritmetica = lambda lista: sum(lista) / len(lista) if len(lista) > 0 else None

# Exemplo de uso
numeros = [10, 20, 30, 40, 50]

# Chamando a função lambda para calcular a média aritmética da lista de números
resultado = media_aritmetica(numeros)

# Imprimindo o resultado
print(resultado)
