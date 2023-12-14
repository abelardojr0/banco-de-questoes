def conta_vogais_consoantes(texto:str):
    # Inicializa contadores para vogais e consoantes
    vogais = 0
    consoantes = 0

    # Itera sobre cada caractere na string
    for letra in texto:
        # Verifica se o caractere é uma vogal
        if letra.lower() in "aeiou":
            vogais += 1
        # Verifica se o caractere é uma consoante (letra do alfabeto que não é vogal)
        elif letra.lower() in "bcdefghjklmnpqrstvxywz":
            consoantes += 1

    # Cria um dicionário com os resultados
    resultado = {"vogais": vogais, "consoantes": consoantes}
    return resultado

# Exemplo de uso
texto = str(input("Digite um texto qualquer: "))
resultado = conta_vogais_consoantes(texto)

print(resultado)
