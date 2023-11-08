# Inicializa os dois primeiros termos da sequência
termo1 = 0
termo2 = 1

# Exibe os primeiros 10 termos da sequência de Fibonacci
print("Os primeiros 10 termos da sequência de Fibonacci:")
for _ in range(10):
    print(termo1, end=" ")
    proximo_termo = termo1 + termo2
    termo1, termo2 = termo2, proximo_termo
