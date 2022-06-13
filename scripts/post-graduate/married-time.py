# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

name = str('')
sex = str('')
marital_status = str('')

married_years = ''

name = input('Seu nome: ')
sex = input('Seu sexo: ')
marital_status = input('Estado civil: ')

print(f'\n')

print(f'Nome: {name}')
print(f'Sexo: {sex}')
print(f'Estado civil : {marital_status}')

if sex == 'F' and marital_status == 'CASADA':
    married_years = str(input('Tempo de casada (anos): '))
    print(f'Tempo de casada (anos): {married_years}')
