d = {
    'name': [],
    'age': [],
    'phone': [],
    'address': []
}

name = input('Nome : ')
age = input('Idade : ')
phone = input('Telefone : ')
address = input('Endereço : ')

d['name'].append(name)
d['age'].append(age)
d['phone'].append(phone)
d['address'].append(address)

print(d)
