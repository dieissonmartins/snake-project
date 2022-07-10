def getAverage(n1, people):
    return sum(n1[people]) / len(n[people])


n = {}

while True:
    name = input('Digite nome do aluno:')
    if not name:
        break

    n_1 = float(input('Digite a primeira nota:'))
    n_2 = float(input('Digite a segunda nota:'))
    n[name] = [n_1, n_3]

max_n = []

for item in n:
    average = getAverage(n, item)
    if max_n:
        if average > max_n[-1]:
            max_n = [item, average]
    else:
        max_n = [item, average]

print(f'maior média do aluno {max_n[0]}: {max_n[1]}')
