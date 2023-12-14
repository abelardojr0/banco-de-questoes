# Definindo a superclasse Funcionario
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def bater_ponto(self, tal_hora):
        return f"O {self.nome} bateu o ponto às {tal_hora}"

# Criando a subclasse Caixa que herda de Funcionario
class Caixa(Funcionario):
    def __init__(self, nome, cpf, salario, num_caixa):
        # Chamando o construtor da superclasse
        super().__init__(nome, cpf, salario)
        self.num_caixa = num_caixa  # Novo atributo específico para a classe Caixa

    # Polimorfismo do método bater_ponto
    def bater_ponto(self, tal_hora):
        return f"O caixa {self.nome} (Caixa {self.num_caixa}) bateu o ponto às {tal_hora}"

# Instanciando um objeto da classe Caixa
caixa1 = Caixa(nome="Maria", cpf="987.654.321-00", salario=6000.0, num_caixa=1)

# Usando o método bater_ponto() e exibindo o resultado
hora_do_ponto = "09:30"
print(caixa1.bater_ponto(tal_hora=hora_do_ponto))
