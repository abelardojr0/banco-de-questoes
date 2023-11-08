# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Inicializa a variável para contar a quantidade de consoantes
contagem_consoantes = 0

# Percorre a frase para contar as consoantes
for letra in frase:
      #Tranforma cada letra em minúsculo para fazer a verificação
    if letra.lower() in "bcdfghjklmnpqrstvwxyz":
        contagem_consoantes += 1

# Exibe a quantidade de consoantes na frase
print(f"A frase contém {contagem_consoantes} consoante(s).")
