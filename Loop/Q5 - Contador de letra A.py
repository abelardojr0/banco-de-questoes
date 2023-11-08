# Solicita ao usuário que digite uma frase
frase = str(input("Digite uma frase: ")).lower()

# Inicializa a variável para contar a quantidade de letras 'a'
contagem_a = 0

# Percorre a frase para contar as letras 'a'
for letra in frase:
    #Tranforma cada letra em minúsculo para fazer a verificação
    if letra.lower() == 'a':
        contagem_a += 1

# Exibe a quantidade de letras 'a' na frase
print(f"A frase contém {contagem_a} letra(s) 'a'.")
