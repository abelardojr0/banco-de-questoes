# Dadas as listas de nomes e idades
nomes = ['Ana', 'João', 'Maria', 'Pedro']
idades = [25, 30, 22, 28]

# Cria um dicionário associando cada nome à sua respectiva idade usando um loop for
dicionario_idades = {}

for i in range(len(nomes)):
    nome = nomes[i]
    idade = idades[i]
    dicionario_idades[nome] = idade

# Imprime o dicionário resultante
print(f"Dicionário de Idades: {dicionario_idades}")
