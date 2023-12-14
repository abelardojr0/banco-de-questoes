# Dada a lista
lista_original = [4, 6, 8, 5, 6, 3, 4, 7, 9, 4, 8]

# Inicializa uma nova lista vazia para armazenar os elementos únicos
lista_sem_duplicatas = []

# Percorre a lista original
for elemento in lista_original:
    # Adiciona o elemento à nova lista apenas se ainda não estiver presente
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)

# Imprime a nova lista sem duplicatas
print(f"Lista sem duplicatas: {lista_sem_duplicatas}")
