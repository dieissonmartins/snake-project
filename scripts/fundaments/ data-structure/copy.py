citys_01 = ['Novo Cruzeiro', 'Belo Horizonte', 'São Paulo', 'Betim', 'Contagem', 'Paracicaba', 'Alpercata']

print(citys_01)

citys_02 = citys_01.copy()

new_position = len(citys_02) + 1

citys_02.insert(new_position, 'New City Insert')

print(citys_02)
