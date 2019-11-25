"""
Exercicio 49
"""


hora1 = int(input("hora: "))
minuto1 = int(input("minuto: "))
segundo1 = int(input("segundo: "))
duracao = int(input("Duração em segundos: "))
print(f"horario de inicio {hora1:02d}:{minuto1:02d}:{segundo1:02d}")
segundo1 = segundo1 + minuto1*60 + hora1*3600
duracao = duracao + segundo1
hora = duracao // 3600
duracao = duracao % 3600
minuto = duracao // 60
duracao = duracao % 60

print(f"horario de término {hora:02d}:{minuto:02d}:{duracao:02d}")
