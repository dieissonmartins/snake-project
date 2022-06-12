# Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

import math

value1 = float(0)

value1 = float(input('digite valor: '))

if value1 % 2 != 0:
    c = (value1 + 8)
else:
    c = (value1 + 5)

print(f'Valor final é: {c}')
