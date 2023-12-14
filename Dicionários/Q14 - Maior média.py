# Dada a lista de dicionários de alunos
alunos = [{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]},
          {'nome': 'João', 'notas': [7.0, 8.5, 9.5]},
          {'nome': 'Maria', 'notas': [9.0, 8.0, 8.5]}]

# Inicializa variáveis para a maior média e o nome do aluno correspondente
maior_media = 0
aluno_maior_media = None

# Itera sobre a lista de dicionários de alunos
for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']
    media = sum(notas) / len(notas)
    
    # Verifica se a média atual é maior que a maior média atual
    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome

# Imprime o nome do aluno com a maior média
print(f"Aluno com a maior média: {aluno_maior_media}")
