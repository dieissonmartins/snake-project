"""
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
    pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
     latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor.
     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""


class PaintStorePallons:

    def __init__(self):
        self.meters_square_paint = float(0.00)
        self.liter_pint_meters = float(6)
        self.can_liters = float(18)
        self.can_liters_money = float(80)
        self.can_pallons = float(3.6)
        self.can_pallons_money = float(25)
        self.meters_square_paint = float(0.00)
        self.total_liters = float(0.00)
        self.pinch_money = float(0.00)
        self.cans_total = float(0.00)
        self.cans_total_pallons = float(0.00)
        self.pinch_money_pallons = float(0.00)
        self.cans_total_rest = float(0.00)
        self.pinch_money_rest = float(0.00)
        self.cans_total_rest2 = float(0.00)
        self.cans_total_pallons_rest = float(0.00)
        self.pinch_money_pallons_rest = float(0.00)

    def calc_quantities_cans(self):
        self.meters_square_paint = float(input('Tamanho em metros quadrados da área a ser pintada'))

        self.total_liters = (self.meters_square_paint / self.liter_pint_meters)

        self.cans_total = (self.total_liters / self.can_liters)
        self.pinch_money = (self.cans_total * self.can_liters_money)

        self.cans_total_pallons = (self.total_liters / self.can_pallons)
        self.pinch_money_pallons = (self.cans_total * self.can_pallons_money)

        self.cans_total_rest = (self.total_liters % self.can_liters)

        self.cans_total_rest2 = ((self.total_liters - self.cans_total_rest) / self.can_liters)
        self.pinch_money_rest = (self.cans_total_rest2 * self.can_liters_money)

        self.cans_total_pallons_rest = (self.cans_total_rest / self.can_pallons)
        self.pinch_money_pallons_rest = (self.cans_total_pallons_rest * self.can_pallons_money)

        print(f'Quantidades latas de {self.can_liters} litros: {round(self.cans_total, 2)}')
        print(f'Preço total latas de {self.can_liters} litros: R$ {round(self.pinch_money, 2)}')

        print(f'ou \n')

        print(f'Quantidades galões de {self.cans_total_pallons} litros: {round(self.pinch_money_pallons, 0)}')
        print(f'Preço total galões de {self.cans_total_pallons} litros: R$ {round(self.pinch_money_pallons, 2)}')

        print(f'ou \n')

        print(f'Quantidades latas de {self.can_liters} litros: {round(self.cans_total_rest2, 2)}')
        print(f'Preço total latas de {self.can_liters} litros: R$ {round(self.pinch_money_rest, 2)}')
        print(f'Quantidades galões de {self.cans_total_pallons_rest} litros: {round(self.pinch_money_pallons_rest, 0)}')
        print(f'Preço total galões de {self.cans_total_pallons_rest} litros: R$ {round(self.pinch_money_pallons_rest, 2)}')


paint_store = PaintStorePallons()
paint_store.calc_quantities_cans()
