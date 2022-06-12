# Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois,
# caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma
# variável C e mostrar seu conteúdo na tela.

value1 = float(0)
value2 = float(0)

value1 = float(input('digite valor A: '))
value2 = float(input('digite valor B: '))

if value1 == value2:
    c = (value1 + value2)
else:
    c = (value1 * value2)

print(f'Valor final é: {c}')
