def inva(d):
    r = {}
    for key, value in zip(d.keys(), d.values()):
        if value in r:
            r[value].append(key)
        else:
            r[value] = [key]
    return r
