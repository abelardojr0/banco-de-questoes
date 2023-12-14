estoque = {
    'Smartphone': 50,
    'Notebook': 30,
    'Fones de ouvido': 100
}

# Menu principal
while True:
    opcao = int(input("""
        Escolha uma opção: 
        1 - Mostrar Estoque
        2 - Adicionar Produto
        3 - Remover Produto
        0 - Sair    
                      """))
    match opcao:
      case 1:
          print("Estado atual do estoque:")
          for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")
      case 2:
        produto = input("Digite o nome do produto a ser adicionado: ")
        quantidade = int(input(f"Digite a quantidade de {produto} a ser adicionada: "))
        if produto in estoque:
            estoque[produto] += quantidade
            print(f"{quantidade} unidades de {produto} foram adicionadas ao estoque.")
        else:
            print(f"Erro: Produto {produto} não encontrado no estoque.")
      case 3:
        produto = input("Digite o nome do produto a ser removido: ")
        quantidade = int(input(f"Digite a quantidade de {produto} a ser removida: "))
        if produto in estoque and estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print(f"{quantidade} unidades de {produto} foram removidas do estoque.")
        else:
            print(f"Erro: Não há unidades suficientes de {produto} no estoque.")
      case 0:
        print("Saindo do programa. Até mais!")
        break
      case _:
        print("Opção inválida. Por favor, escolha uma opção válida.")
