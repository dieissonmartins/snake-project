pasta = float(0)
height = float(0)
imc = float(0)

pasta = float(input('Digite seu peso (em kg): '))
height = float(input('Digite sua altura (em metros): '))

imc = float(pasta / (height * height))

if imc < 18.5:
    print(f'IMC: {imc}\tAbaixo do peso\n')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc}\tPeso normal\n')
elif 25 <= imc < 30:
    print(f'IMC: {imc}\tSobrepeso\n')
elif 30 <= imc < 35:
    print(f'IMC: {imc}\tObesidade grau 1\n')
elif 35 <= imc < 40:
    print(f'IMC: {imc}\tObesidade grau 2\n')
else:
    print(f'IMC: {imc}\tObesidade grau 3\n')
