# Definindo a superclasse Funcionario
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def bater_ponto(self, hora):
        return f"O {self.nome} bateu o ponto às {hora}"

# Criando a subclasse Gerente que herda de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, num_caixa):
        # Chamando o construtor da superclasse
        super().__init__(nome, cpf, salario)
        self.num_caixa = num_caixa  # Novo atributo específico para a classe Gerente

    # Polimorfismo do método bater_ponto
    def bater_ponto(self, hora):
        return "Gerente não bate ponto"

    # Novo método específico para a classe Gerente
    def demitir(self, demitido):
        return f"O gerente {self.nome} demitiu o funcionário {demitido}"

# Instanciando um objeto da classe Gerente
caixa1 = Gerente(nome="João", cpf="123.456.789-00", salario=4000.0, num_caixa=1)

# Usando o método bater_ponto() e o novo método demitir()
hora_do_ponto = "08:00"
print(caixa1.bater_ponto(hora=hora_do_ponto))
print(caixa1.demitir(demitido="Maria"))
