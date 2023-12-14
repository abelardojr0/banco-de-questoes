# Cria o dicionário aluno
aluno = {
    'nome': 'João',
    'notas': [8.5, 9.0, 7.8],
    'faltas': 2
}

# Calcula a média das notas
media_notas = sum(aluno['notas']) / len(aluno['notas'])

# Imprime a média das notas
print(f"Média das notas do aluno {aluno['nome']}: {media_notas:.2f}")
