class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def bater_ponto(self, hora):
        return f"O {self.nome} bateu o ponto às {hora}"

# Instanciando um objeto da classe Funcionario
meu_funcionario = Funcionario(nome="João", cpf="123.456.789-00", salario=5000.0)

# Usando o método bater_ponto() e exibindo o resultado
hora_do_ponto = "08:00"
print(meu_funcionario.bater_ponto(hora=hora_do_ponto))
