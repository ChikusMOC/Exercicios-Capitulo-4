"""
Exercicio 52
"""


apost1 = float(input("valor 1: "))
apost2 = float(input("valor 2: "))
apost3 = float(input("valor 3: "))
valor_premio = (float(input("Valor premio: ")))

apost_total = apost1 + apost2 + apost3
apost1 = (apost1*valor_premio)/apost_total
apost2 = (apost2*valor_premio)/apost_total
apost3 = (apost3*valor_premio)/apost_total
print(f"Do premio {valor_premio} cada um irá receber {apost1}, {apost2}, {apost3}")
