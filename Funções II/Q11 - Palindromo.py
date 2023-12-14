# Definindo uma função lambda que verifica se uma string é um palíndromo
eh_palindromo = lambda s: s == s[::-1]

# Exemplos de uso
texto = str(input("Digite um texto: "))

# Testando a função lambda
resultado = eh_palindromo(texto)

# Imprimindo os resultados
if resultado:
  print(f'A string "{texto}" é palíndromo')
else:
  print(f'A string "{texto}" não é palíndromo')

