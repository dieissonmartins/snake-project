go_out = False
is_go_out = 0
d = []

while not go_out:
    cpf = input('Digite cpf:')
    name = input('Digite nome:')
    age = input('Digite idade:')
    phone = input('Digite telefone:')

    key = str(name) + '-' + str(age) + str(phone)

    d.append([cpf, name, age, phone])

    if not go_out:
        is_go_out = int(input('0 - para continuar \n 1 - para sair:'))

    if is_go_out == 1:
        break

print(d)
