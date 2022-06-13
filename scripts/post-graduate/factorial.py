# Escrever um programa que leia 3 valores A, B e C, e os escreva em ordem crescente.

factorials = []

factorials_count = int(input('Digite quatidade de valores a digitar: '))

i = 1

while i <= factorials_count:
    factorials.append(float(input(f'digite valor {i}: ')))
    i += 1

for number in factorials:

    result = 1
    count = 1

    while count <= number:
        result *= count
        count += 1

        print(result)

    print('-----------')
