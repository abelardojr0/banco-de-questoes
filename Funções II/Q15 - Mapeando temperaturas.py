# Lista original de temperaturas em Celsius
temperaturas_celsius = [0, 10, 20, 30, 40]

# Utilizando map e uma função lambda para converter as temperaturas para Fahrenheit
temperaturas_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))

# Exibindo a lista resultante
print(temperaturas_fahrenheit)
