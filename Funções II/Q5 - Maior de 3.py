# Definindo uma função lambda que retorna o maior de três números (x, y, z)
maior_numero = lambda x, y, z: max(x, y, z)

# Exemplo de uso
# Definindo três números para encontrar o maior entre eles
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Chamando a função lambda para encontrar o maior número
resultado = maior_numero(numero1, numero2, numero3)

# Imprimindo o resultado
print(resultado)
