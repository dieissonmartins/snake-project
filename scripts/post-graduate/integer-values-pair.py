# Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

import math

value1 = float(0)

value1 = float(input('digite valor: '))

if value1 % 2 != 0:
    c = (value1 + 8)
else:
    c = (value1 + 5)

print(f'Valor final é: {c}')
