"""
Exercicio 30 - Leia um valor em real e a cotação do dolar. Em seguida, imprima o valor correspondente em dolares.
"""


real = float(input("valor em real: "))
dolar = float(input("cotação do dolar: "))

real_dolar = real/dolar

print(f"o valor {real} convertido em dolar = {real_dolar}")
