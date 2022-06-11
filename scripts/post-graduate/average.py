"""
 Faça um Programa que peça as 4 notas bimestrais e mostre a média
"""


class Average:

    def __init__(self):
        self.average = float(0.00)
        self.var1 = float(0.00)
        self.var2 = float(0.00)
        self.var3 = float(0.00)
        self.var4 = float(0.00)

    def calc_average(self):
        self.var1 = float(input('Digite valor1:'))
        self.var2 = float(input('Digite valor2:'))
        self.var3 = float(input('Digite valor3:'))
        self.var4 = float(input('Digite valor4:'))

        self.average = (self.var1 + self.var2 + self.var3 + self.var3) / 4

        print(f'+ Média das notas é: {self.average}')


ideal_weight = Average()
ideal_weight.calc_average()
