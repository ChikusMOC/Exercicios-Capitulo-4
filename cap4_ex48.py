"""
Exercicio 48
"""


segundos = int(input("segundos: "))

hora = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60
print(f"{hora}:{minutos}:{segundos}")
