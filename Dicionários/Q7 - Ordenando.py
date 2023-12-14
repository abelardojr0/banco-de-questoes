# VERSÃO COM RECURSOS
# Dada a lista de dicionários de alunos
alunos = [{'nome': 'Ana', 'nota': 8.5}, {'nome': 'João', 'nota': 7.0}, {'nome': 'Maria', 'nota': 9.5}]

# Ordena a lista com base nas notas em ordem decrescente usando o método sort
alunos.sort(key=lambda aluno: aluno['nota'], reverse=True)

# Imprime a lista de alunos ordenada
print("Lista de Alunos Ordenada por Notas (em ordem decrescente):")
for aluno in alunos:
    print(aluno)



# VERSÃO SEM RECURSOS

# Dada a lista de dicionários de alunos
alunos = [
    {
        'nome': 'Ana',
        'nota': 8.5
    },
    {
        'nome': 'João',
        'nota': 7.0
    },
    {
        'nome': 'Maria',
        'nota': 9.5
    }
    ]

# Implementa o algoritmo de ordenação de bolhas (bubble sort)
n = len(alunos)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if alunos[j]['nota'] < alunos[j + 1]['nota']:
            # Troca os elementos se estiverem fora de ordem
            alunos[j], alunos[j + 1] = alunos[j + 1], alunos[j]

# Imprime a lista de alunos ordenada
print("Lista de Alunos Ordenada por Notas (em ordem decrescente):")
for aluno in alunos:
    print(aluno)
