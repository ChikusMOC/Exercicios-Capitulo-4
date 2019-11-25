"""
Exercicio 47
"""


numero = int(input("numero: "))
if 1000 <= numero <= 9999:
    #numero = numero.__str__()
    #for i in range(4):
    #    print(f"{tuple(numero)[i]}")
    n1 = numero//1000
    n2 = numero//100 - n1*10
    n3 = numero//10 - n1*100 - n2*10
    n4 = numero%10
    print(f"{n1}\n{n2}\n{n3}\n{n4}")
else:
    print("Numero informado esta fora do range permitido.")
