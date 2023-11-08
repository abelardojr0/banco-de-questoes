# Solicita ao usuário que digite sua senha
senha = str(input("Digite sua senha: "))

# Inicializa variáveis para controlar as condições da senha
qtde_caracters = False
contem_minuscula = False
contem_maiuscula = False
contem_numero = False
contem_especial = False

# Define listas de caracteres para verificar as condições
alfabeto = "abcdefghijklmnopqrstuvxywz"
numeros = "012345789"
caracteres_especiais = "!@#$%^&*()_+-=[]{|};:'<>,.?/~"

# Verifica se a senha tem pelo menos 8 caracteres
if len(senha) >= 8:
    qtde_caracters = True

# Percorre cada caractere na senha para verificar as outras condições
for caracter in senha:
    if caracter in alfabeto:
        contem_minuscula = True
    elif caracter in alfabeto.upper():
        contem_maiuscula = True
    elif caracter in numeros:
        contem_numero = True
    elif caracter in caracteres_especiais:
        contem_especial = True

# Verifica se a senha atende a todas as condições
if qtde_caracters and contem_minuscula and contem_maiuscula and contem_numero and contem_especial:
    print("Senha válida")
else:
    print("Senha inválida")
