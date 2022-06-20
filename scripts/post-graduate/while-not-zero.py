n = c = int(0)

while n != 0:
    n = int(input('Digite valor: '))
    if 100 <= n <= 200:
        c = (c + 1)

    print(f'quantidade de numero entre 100 e 200 digitados: {c}')
