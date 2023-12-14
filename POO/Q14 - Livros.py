class Livro:
    def __init__(self, nome, autor, num_paginas, genero):
        self.nome = nome
        self.autor = autor
        self.num_paginas = num_paginas
        self.genero = genero
    
    def ver_informacoes(self):
        return f"Nome: {self.nome}\nAutor: {self.autor}\nNúmero de Páginas: {self.num_paginas}\nGênero: {self.genero}"

# Instanciando um objeto da classe Livro
meu_livro = Livro(nome="Dom Casmurro", autor="Machado de Assis", num_paginas=256, genero="Romance")

# Chamando o método ver_informacoes() e exibindo o resultado
informacoes_livro = meu_livro.ver_informacoes()
print(informacoes_livro)
