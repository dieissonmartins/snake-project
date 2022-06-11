# Escrever um programa que leia 3 valores A, B e C, e os escreva em ordem crescente.

letters = []

letters.append(float(input('digite valor 1: ')))
letters.append(float(input('digite valor 2: ')))
letters.append(float(input('digite valor 3: ')))

letters.sort()

print(letters)
