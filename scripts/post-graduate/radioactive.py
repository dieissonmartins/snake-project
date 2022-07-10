tmp_tt = tmp_hr = tmp_mm = tmp_sg = int(0)
ms_start = ms_end = float(0)

ms_start = float(input('Massa Inicial (em Gramas):'))

ms_end = ms_start

while ms_end >= 0.5:
    ms_end = (ms_end / 2)
    tmp_tt = (tmp_tt + 50)

print('\n')
print(f'Massa Inicial: {ms_start} gramas')
print(f'Massa Final: {ms_end} gramas')

print('\n')
print(f'Tempo total {tmp_tt} segundos \n')

tmp_hr = (tmp_tt / 3600)
tmp_mm = ((tmp_tt % 3600) / 60)
tmp_sg = ((tmp_tt % 3600) % 60)

print(f'Tempo Dividido: {tmp_hr} horas: {tmp_mm} minutos: {tmp_sg} segundos.')
