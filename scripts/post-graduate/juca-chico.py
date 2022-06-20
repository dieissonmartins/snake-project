tam_chico = int(150)
tam_juca = int(110)
y = int(0)

while tam_juca <= tam_chico:
    tam_chico = (tam_chico + 2)
    tam_juca = (tam_chico + 3)
    y = (y + 1)

print(f'Serão necessário {y} Anos para que Juca seja maior do que Chico.')
