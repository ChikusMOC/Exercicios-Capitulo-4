"""
Exercicio 53
"""


comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))
preco_tela = float(input("Preço do metro da tela: "))

valor = 2*(comprimento+largura) * preco_tela

print(f"Você irá gastar R${valor} para cercar seu terreno")
