import random

v_sum = n = r = int(0)

n = int(input('Informe valor:'))

while r != n:
    r = random.randrange(1, 11, 1)
    v_sum = (v_sum + r)
    print(f'numero: {r}')
    print(f'soma: {v_sum}')
    print(f'--------')

print(f'soma dos aleatorios: {v_sum}')
