class Livro:
    def __init__(self, nome, autor, num_paginas, genero):
        self.nome = nome
        self.autor = autor
        self.num_paginas = num_paginas
        self.genero = genero
    
    def ver_informacoes(self):
        return f"""
            Nome: {self.nome}
            Autor: {self.autor}
            Número de Páginas: {self.num_paginas}
            Gênero: {self.genero}"""

# Lista para armazenar os livros
biblioteca = []

# Função para adicionar um novo livro
def adicionar_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    num_paginas = int(input("Digite o número de páginas: "))
    genero = input("Digite o gênero do livro: ")

    novo_livro = Livro(nome, autor, num_paginas, genero)
    biblioteca.append(novo_livro)
    print(f"Livro '{nome}' adicionado à biblioteca!")

# Função para ver todas as informações de todos os livros
def ver_todos_os_livros():
    if not biblioteca:
        print("A biblioteca está vazia.")
        return
    
    print("Todos os livros na biblioteca:")
    for livro in biblioteca:
        print(livro.ver_informacoes())

# Função para editar um livro
def editar_livro():
    ver_todos_os_livros()

    if not biblioteca:
        return

    try:
        indice = int(input("Escolha o número do livro que deseja editar:")) 
        livro_para_editar = biblioteca[indice]

        print("Escolha o campo que deseja editar:")
        print("1 - Nome")
        print("2 - Autor")
        print("3 - Número de Páginas")
        print("4 - Gênero")

        escolha = int(input("""Digite o número da opção:
        1 - Nome
        2 - Autor
        3 - Número de Páginas
        4 - Gênero
         """))

        if escolha == 1:
            novo_nome = input("Digite o novo nome: ")
            livro_para_editar.nome = novo_nome
        elif escolha == 2:
            novo_autor = input("Digite o novo autor: ")
            livro_para_editar.autor = novo_autor
        elif escolha == 3:
            nova_pagina = int(input("Digite o novo número de páginas: "))
            livro_para_editar.num_paginas = nova_pagina
        elif escolha == 4:
            novo_genero = input("Digite o novo gênero: ")
            livro_para_editar.genero = novo_genero
        else:
            print("Opção inválida.")
            return

        print(f"Livro '{livro_para_editar.nome}' editado com sucesso!")

    except IndexError:
        print("Índice inválido. Por favor, escolha um número válido.")

# Função para excluir um livro
def excluir_livro():
    ver_todos_os_livros()

    if not biblioteca:
        return

    try:
        indice = int(input("Escolha o número do livro que deseja excluir: ")) - 1
        livro_excluido = biblioteca.pop(indice)
        print(f"Livro '{livro_excluido.nome}' excluído da biblioteca.")

    except IndexError:
        print("Índice inválido. Por favor, escolha um número válido.")

# Menu principal
while True:
    print("Menu:")


    escolha_menu = int(input("""Digite o número da opção desejada:
    1 - Adicionar livro
    2 - Ver todos os livros
    3 - Editar livro
    4 - Deletar livro
    0 - Sair 
    """))
    match escolha_menu:
    
        case 1:
            adicionar_livro()
        case 2:
            ver_todos_os_livros()
        case 3:
            editar_livro()
        case 4:
            excluir_livro()
        case 0:
            print("Saindo do programa.")
            break
        case _:
            print("Opção inválida. Tente novamente.")
    
    input("Pressione Enter para continuar...")
