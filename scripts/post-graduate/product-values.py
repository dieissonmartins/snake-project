i = j = number = int(0)

i = int(92)
m = int(1478)

while i <= m:
    number = int(0)
    j = int(2)
    while j < i:
        if i % j == 0:
            j = i
            number = 1
    j = j + 1

    print(f'produto dos números primos entre {i} e {m}: {i} \n')

print(f'fim')
