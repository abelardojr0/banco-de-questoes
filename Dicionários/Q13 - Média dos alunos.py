#VERSÃO COM RECURSOS

# Dada a lista de dicionários de alunos
alunos = [
    {'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]},
    {'nome': 'João', 'notas': [7.0, 8.5, 9.5]},
    {'nome': 'Maria', 'notas': [9.0, 8.0, 8.5]}
    ]

# Inicializa uma lista para armazenar as médias dos alunos
medias_alunos = []

# Calcula a média de cada aluno e adiciona à lista
for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']
    media = sum(notas) / len(notas)
    medias_alunos.append({'nome': nome, 'media': media})

# Ordena a lista de médias em ordem crescente
medias_alunos.sort(key=lambda aluno: aluno['media'])

# Imprime a lista de médias em ordem crescente
print("Médias dos Alunos em Ordem Crescente:")
for aluno in medias_alunos:
    print(f"{aluno['nome']}: {aluno['media']:.2f}")




# VERSÃO SEM RECURSOS
# Dada a lista de dicionários de alunos
alunos = [{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]},
          {'nome': 'João', 'notas': [7.0, 8.5, 9.5]},
          {'nome': 'Maria', 'notas': [9.0, 8.0, 8.5]}]

# Calcula a média de cada aluno e cria uma lista de tuplas (nome, média)
medias_alunos = [(aluno['nome'], sum(aluno['notas']) / len(aluno['notas'])) for aluno in alunos]

# Implementa um algoritmo de ordenação manual (Seleção)
for i in range(len(medias_alunos)):
    menor_idx = i
    for j in range(i + 1, len(medias_alunos)):
        if medias_alunos[j][1] < medias_alunos[menor_idx][1]:
            menor_idx = j
    medias_alunos[i], medias_alunos[menor_idx] = medias_alunos[menor_idx], medias_alunos[i]

# Imprime a lista de médias em ordem crescente
print("Médias dos Alunos em Ordem Crescente:")
for nome, media in medias_alunos:
    print(f"{nome}: {media:.2f}")

