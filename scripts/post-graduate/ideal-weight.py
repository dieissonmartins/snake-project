"""
  Tendo como dado de entrada a altura (h) de uma pessoa,
 construa um algoritmo que calcule seu peso ideal,
 utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""


class IdealWeight:

    def __init__(self, h):
        self.h = float(h)

    def calc_ideal_weight_man(self):
        h = self.h
        ideal_weight_man = round(((72.7 * h) - 58), 2)

        print(f'Peso ideal para homens é: {ideal_weight_man} \n')

    def calc_ideal_weight_women(self):
        h = self.h
        ideal_weight_women = round(((62.1 * h) - 44.7), 2)

        print(f'Peso ideal para mulheres é: {ideal_weight_women} \n')


ideal_weight = IdealWeight(1.80)
ideal_weight.calc_ideal_weight_man()
ideal_weight.calc_ideal_weight_women()