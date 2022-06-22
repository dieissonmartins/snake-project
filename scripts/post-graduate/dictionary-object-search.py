def find_aux(aux, key):

    new_aux = []

    for key_aux, item in aux.items():
        if item == key:
            new_position = len(new_aux) + 1
            new_aux.insert(new_position, key_aux)

    return new_aux


aux = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 4
}

itens = find_aux(aux, 1)

print(itens)
