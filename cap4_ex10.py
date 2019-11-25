"""
Exercicio 10 - Leia uma velocidade em km/h e apresente-a convertida em m/s. A formula de conversão é:
M = K/3.6, sendo K a velocidade em km/h e M em m/s.
"""


vel_k = float(input("Digite a velocidade em km/h: "))
vel_m = vel_k/3.6

print(f"A velocidade {vel_k} convertida para m/s = {vel_m}")
