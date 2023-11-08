# Solicita ao usuário que insira uma nota até que seja válida
while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    
    if 0 <= nota <= 10:
        break
    else:
        print("Valor inválido. Por favor, insira uma nota entre 0 e 10.")

# Após sair do loop, exibe a nota válida
print(f"A nota válida inserida é: {nota}")
