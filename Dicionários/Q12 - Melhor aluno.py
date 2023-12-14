# Dado o dicionário de notas dos alunos
notas_alunos = {
    'Ana': [8.0, 7.5, 9.0], 
    'João': [7.0, 8.5, 9.5],
    'Maria': [9.0, 8.0, 8.5]}

# Inicializa variáveis para armazenar as melhores notas e o nome do aluno correspondente
melhores_notas = 0
aluno_melhores_notas = ""

# Itera sobre o dicionário de notas
for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    if media > melhores_notas:
        melhores_notas = media
        aluno_melhores_notas = aluno

# Imprime o nome e a média do aluno com as melhores notas
print(f"Aluno com as melhores notas: {aluno_melhores_notas}")
print(f"Média: {melhores_notas:.2f}")
