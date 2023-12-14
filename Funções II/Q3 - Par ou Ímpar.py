# Definindo uma função lambda que verifica se um número (x) é par ou ímpar
par_ou_impar = lambda x: "Par" if x % 2 == 0 else "Ímpar"

# Exemplo de uso
# Definindo um número para verificar se é par ou ímpar
numero = int(input("Digite um número: "))

# Chamando a função lambda para determinar se o número é par ou ímpar
resultado = par_ou_impar(numero)

# Imprimindo o resultado
print(resultado)
