go_out = False
is_go_out = 0
d = []
d2 = []

while not go_out:
    cpf = input('Digite cpf:')
    name = input('Digite nome:')
    age = int(input('Digite idade:'))

    d.append([cpf, name, age])

    if not go_out:
        is_go_out = int(input('0 - para continuar \n 1 - para sair:'))

    if is_go_out == 1:
        break

for i, row in d:
    if row[2] < 18:
        d.append([row])
        del d[i]

print(d)
print('------')
print(d2)
