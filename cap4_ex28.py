"""
Exercicio 28 - Faça a leitura de três valores e apresete como resultado a soma dos quadrados dos três valores lidos.
"""


print("informe três valores")
num1 = float(input("primeiro valor: "))
num2 = float(input("segundo valor: "))
num3 = float(input("terceiro valor: "))
total = num1**2 + num2**2 + num3**2

print(f"{num1}²+{num2}²+{num3}² = {total}")
