# Definindo uma função lambda que verifica se uma idade (idade) é maior ou menor de idade
verifica_idade = lambda idade: "Maior de idade" if idade >= 18 else "Menor de idade"

# Exemplo de uso
# Definindo uma idade para verificar se é maior ou menor de idade
idade_usuario = int(input("Digite um número: "))

# Chamando a função lambda para determinar se a idade é maior ou menor de idade
resultado = verifica_idade(idade_usuario)

# Imprimindo o resultado
print(resultado)
