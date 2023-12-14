def filtrar_emails(lista_emails):
    # Inicializa a lista para armazenar os e-mails do Gmail
    emails_gmail = []

    # Itera sobre cada e-mail na lista
    for email in lista_emails:
        # Verifica se o e-mail pertence ao domínio do Gmail
        if email.endswith('@gmail.com'):
            emails_gmail.append(email)

    return emails_gmail

# Exemplo de uso
lista_de_emails = [
    'user1@gmail.com',
    'user2@yahoo.com',
    'user3@gmail.com',
    'user4@hotmail.com'
]

emails_do_gmail = filtrar_emails(lista_de_emails)

# Imprime a nova lista contendo apenas os e-mails do Gmail
print(emails_do_gmail)
