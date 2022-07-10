n = odd = pair = int(0)

while n < 1000:
    n = int(input('Digite valor: '))

    if n % 2 != 0:
        odd += n
    else:
        pair += n

print(f'soma pares {pair}')
print(f'soma impares {odd}')
