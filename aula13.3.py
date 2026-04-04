Horas = input ("Digite que horas são: ")
Horas = float(Horas)
if 0 <= Horas <= 11:
    print(f'Bom dia, são {Horas} horas')
elif 12 <= Horas <= 17:
    print(f'Boa tarde, são {Horas} horas')
elif 18 <= Horas <= 24:
    print(f'Boa noite, são {Horas} horas')
else:
    print(f'Error: Você não digitou as horas, você digitou {Horas}')
