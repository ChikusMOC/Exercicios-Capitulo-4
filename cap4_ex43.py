"""
Exercicio 43
"""


valor = float(input("valor: "))
total1 = valor - valor*0.1
total2 = valor/3
com1 = total1 *0.05
com2 = valor*0.05

print(f"Mercadoria = {valor}. A vista = {total1}. Parcelado em 3x{total2}. "
      f"Comissão na venda à vista {com1}. Comissão na venda a prazo {com2}")
