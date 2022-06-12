price = float(0)
opc = float(0)
c = float(0)

price = float(input('Digite o preco da etiqueta: '))
opc = int(input('Digite a forma de pagamento: '))

if opc == 1:
    c = price * 0.85
    print('Ganhaste 15% off!')
    print(f'Preco final eh: {c}')
elif opc == 2:
    c = price * 0.90
    print('Ganhaste 10% off!')
    print(f'Preco final eh: {c}')
elif opc == 3:
    print(f'Preco sem desconto: {c}')
elif opc == 4:
    c = price * 1.10
    print('Acrescimeo de 10%!')
    print(f'Preco final eh: {c}')
