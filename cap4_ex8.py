"""
Exercicio 8 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A formula de conversão é: C = K -273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""


kelvin = float(input("Digite a temperatura em kelvin: "))

print(f"A temperatura {kelvin} convertida para Celsius = {kelvin - 273.15}")
