def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Exemplo de uso
temperatura_celsius = int(input("Digite uma temperatura em graus celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

print(f'{temperatura_celsius} graus Celsius é igual a {temperatura_fahrenheit:.2f} graus Fahrenheit.')
