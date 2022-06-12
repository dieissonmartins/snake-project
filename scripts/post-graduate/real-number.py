"""
Faça um programa, utilizando estrutura de condição, que receba um número real, digitado pelo usuário e mostre o menu
para selecionar o tipo de cálculo que deve ser realizado com base nos códigos abaixo:

101-Raiz quadrada
102-A metade
103-10% do número
104-O dobro
"""
import math

number = float(0)

number = float(input('Digite valor real: '))

print('* 101-Raiz quadrada')
print('* 102-A metade')
print('* 103-10% do número')
print('* 104-O dobro')

action = int(input('Acão: '))

match action:
    case 101:
        source = float(math.sqrt(number), 2)
        print(f'\nA raiz quadrada de {number} é {source}\n')
    case 102:
        a_half = (number / 2)
        print(f'\nA medate de {number} é {a_half}\n')
    case 103:
        percentage = (number * 0.10)
        print(f'\nA 10% do número de {number} é {percentage}\n')
    case 104:
        double = (number * 2)
        print(f'\nA Dobro de {number} é {double}\n')