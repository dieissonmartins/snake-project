phones = {}


def add_name(name, phones1):
    phones1[name] = phones


def add_phone(name, phone):
    if name in phones:
        phones[name].append(phone)


def delete_name(name):
    if name in phones:
        del phones[name]


def delete_phone(name, phone):
    if name in phones:
        if phone in phones[name]:
            phones[name].remove(phone)
    if not phones[name]:
        delete_name(name)


def get_phone(name):
    if name in phones:
        return phones[name]
