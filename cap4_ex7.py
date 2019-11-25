"""
Exercicio 7 - Leia uma temperatura em Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversão é: C = 5.0*(F - 32.0)/9.0, sento C a temperatura em Celsius
e F a temperatura em Fahrenheit.
"""


fahren = float(input("Digite a temperatura em Fahrenheit: "))

print(f"A temperatura {fahren} em Celsius = {5.0*(fahren - 32.0)/9.0}")
