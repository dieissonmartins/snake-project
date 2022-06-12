"""
Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta
 e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler
 qual a condição de pagamento escolhida e efetuar o cálculo adequado.

Código Condição de pagamento

À vista em dinheiro ou cheque, recebe 10% de desconto
À vista no cartão de crédito, recebe 15% de desconto
Em duas vezes, preço normal de etiqueta sem juros
Em duas vezes, preço normal de etiqueta mais juros de 10%
"""

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
