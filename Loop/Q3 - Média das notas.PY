# Inicializa a variável para armazenar a soma das notas
soma_notas = 0

# Solicita ao usuário que digite 8 notas
for i in range(1,9):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma_notas += nota

# Calcula a média das notas
media = soma_notas / 8

# Exibe a média das notas
print(f"A média das notas é: {media:.2f}")
