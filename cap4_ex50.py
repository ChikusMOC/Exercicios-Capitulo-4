"""
Exercicio 50
"""


idade_atual = int(input("Idade: "))
ano = int(input("Ano: "))
verificador = input("você já fez aniversario esse ano S/N? ")
verificador = verificador.upper()

if verificador == "S":
    ano_nascimento = ano - idade_atual
else:
    ano_nascimento = ano - idade_atual - 1

print(f"Você nasceu no ano {ano_nascimento}")
