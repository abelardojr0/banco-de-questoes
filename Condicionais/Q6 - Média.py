# Solicita que o usuário digite as três notas e armazena os valores nas variáveis 'nota1', 'nota2' e 'nota3'
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Verifica se a média está entre 7 e 10 (inclusive)
if media >= 7 and media <= 10:
    # Se a condição for verdadeira, imprime uma mensagem informando que a média é maior que 7 e o aluno foi aprovado
    print(f"Sua média foi {media}, você foi aprovado")

# Caso a condição acima seja falsa, verifica se a média está entre 0 e 7 (inclusive)
elif media < 7 and media >= 0:
    # Se essa condição for verdadeira, imprime uma mensagem informando que a média é menor que 7 e o aluno foi reprovado
    print(f"Sua média foi {media}, você foi reprovado")

# Se ambas as condições acima forem falsas, significa que a média está fora do intervalo válido (fora de 0 a 10)
else:
    # Nesse caso, imprime uma mensagem informando que a média é inválida e que as notas devem estar entre 0 e 10
    print("Média inválida, as notas devem ser um número entre 0 e 10")
