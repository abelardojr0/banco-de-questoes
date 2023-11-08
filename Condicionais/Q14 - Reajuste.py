# Solicita ao usuário que digite o salário
salario = float(input("Digite o seu salário: "))

# Calcula o reajuste com base nas faixas salariais
if salario < 5000:
    reajuste = salario * 0.15
elif 5000 <= salario <= 10000:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05

# Calcula o novo salário com o reajuste
novo_salario = salario + reajuste

# Exibe o resultado arredondado duas casas pós virgula
print(f"O seu salário reajustado é: R${novo_salario:.2f}")
