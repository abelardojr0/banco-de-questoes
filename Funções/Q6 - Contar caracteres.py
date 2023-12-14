def conta_caracteres(texto):
    contador = 0
    for letra in texto:
        if letra != ' ':
            contador += 1
    return contador

# Exemplo de uso
texto = str(input("Digite um texto qualquer: "))
resultado = conta_caracteres(texto)

print(f"O texto {texto} possui {resultado} caracteres")
