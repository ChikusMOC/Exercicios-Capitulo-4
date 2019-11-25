"""
Exercicio 46
"""


numero = int(input("numero: "))
print(f"numero informado {numero}")
numeroinv = 0

if 100 <= numero <= 999:
    while numero > 0:
        numeroinv = numeroinv * 10 + numero % 10
        numero = numero // 10
    print(f"{numeroinv}")

else:
    print("numero informado esta fora do padrao.")
