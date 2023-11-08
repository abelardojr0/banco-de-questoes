# Solicita que o usuário digite uma letra e armazena o valor na variável 'letra'
letra = str(input("Digite uma letra qualquer: ")).lower().strip()

# Converte a entrada do usuário para letras minúsculas (usando .lower()) e remove espaços extras (usando .strip())

# Verifica se 'letra' está contida na string "aeiou" (vogais)
if letra in "aeiou":
    # Se a condição for verdadeira, imprime uma mensagem informando que a letra é uma vogal
    print(f"A letra '{letra}' é uma vogal")

# Caso a condição acima seja falsa, verifica se 'letra' está contida na string "bcdfghjklmnpqrstvxywz" (consoantes)
elif letra in "bcdfghjklmnpqrstvxywz":
    # Se essa condição for verdadeira, imprime uma mensagem informando que a letra é uma consoante
    print(f"A letra '{letra}' é uma consoante")

# Se ambas as condições acima forem falsas, significa que a entrada do usuário não é nem uma vogal nem uma consoante
else:
    # Nesse caso, imprime uma mensagem informando que a entrada deve ser uma letra do alfabeto
    print(f"Digite apenas letras que estejam no alfabeto")
