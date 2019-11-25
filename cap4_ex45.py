"""
Exercicio 45
"""


letra = input("digite uma letra: ")

num = ord(letra)
if 65 <= num <= 90:
    num = num + 32
    letra = chr(num)
    print(f"{letra}")
else:
    if 97 <= num <= 122:
        print(f"{letra}")
