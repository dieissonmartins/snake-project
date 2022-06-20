n = int(0)

n = int(input('Digite valor: '))

odd = i = n
while odd < (i + 10):
    odd = (odd + 1)
    if odd % 2 == 0:
        print(f'Par: {odd}')

pair = i = n
while pair < (i + 10):
    pair = (pair + 1)
    if pair % 2 == 1:
        print(f'Impar: {pair}')
