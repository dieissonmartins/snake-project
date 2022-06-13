# Faça um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do próximo dia.
# Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias.
# (Dica: um ano é bissexto quando for divisível por 4)

import datetime

# get today
dt_today = datetime.datetime.today().date()
dt_today_add_day = dt_today + datetime.timedelta(days=1)

print(f'Hoje é {dt_today.strftime("%d/%m/%Y")}')
print(f'Amanhã é {dt_today_add_day.strftime("%d/%m/%Y")}')
