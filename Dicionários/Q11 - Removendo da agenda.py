# Dado o dicionário de agenda
agenda = {
    'Ana': '555-1234', 
    'João': '555-5678',
    'Maria': '555-4321'
  }

# Solicita ao usuário escolher o nome de uma pessoa
nome_a_remover = str(input("Digite o nome da pessoa a ser removida da agenda: "))

# Verifica se o nome está no dicionário antes de remover
if nome_a_remover in agenda:
    # Remove a pessoa escolhida do dicionário
    del agenda[nome_a_remover]
    print(f"{nome_a_remover} removido da agenda.")
else:
    print(f"{nome_a_remover} não encontrado na agenda.")

# Imprime a agenda atualizada
print(f"Agenda Atualizada: {agenda}")
