def avaliar_senha(senha):
    # Verifica o comprimento da senha
    comprimento = len(senha)
    alfabeto = "abcdefghjklmnopqrstuvxywz"

    # Verifica se há pelo menos 1 letra minúscula
    tem_minuscula = 0
    for letra in senha:
        if letra in alfabeto:
            tem_minuscula = 1
            break

    # Verifica se há pelo menos 1 letra maiúscula
    tem_maiuscula = 0
    for letra in senha:
        if letra in alfabeto.upper():
            tem_maiuscula = 1
            break
        
    # Verifica se há pelo menos um caractere especial
    tem_especial = 0
    for letra in senha:
        if letra in '{[!@#$%^&*(),.?":}|<>]':
                tem_especial = 1
                break

    # Verifica se há pelo menos 1 número
    tem_numero = 0
    for letra in senha:
        if letra in "0123456789":
            tem_numero = 1
            break

    # Conta quantos requisitos são atendidos
    requisitos_atendidos = tem_minuscula + tem_maiuscula + tem_especial + tem_numero

    # Classifica a senha com base nos requisitos atendidos
    if comprimento >= 8 and requisitos_atendidos == 4:
        return "Senha forte"
    elif 2 <= requisitos_atendidos <= 4:
        return "Senha média"
    else:
        return "Senha fraca"

# Exemplo de uso
senha_usuario = input("Digite a senha: ")
classificacao = avaliar_senha(senha_usuario)
print(classificacao)
