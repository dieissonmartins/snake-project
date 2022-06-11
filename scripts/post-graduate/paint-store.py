"""
  Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
 litros,que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""


class PaintStore:

    def __init__(self):
        self.meters_square_paint = float(0.00)
        self.liter_pint_meters = float(3)
        self.can_liters = float(18)
        self.can_liters_money = float(80)
        self.meters_square_paint = float(0.00)
        self.total_liters = float(0.00)
        self.pinch_money = float(0.00)
        self.cans_total = float(0.00)

    def calc_quantities_cans(self):
        self.meters_square_paint = float(input('Tamanho em metros quadrados da área a ser pintada'))

        self.total_liters = (self.meters_square_paint / self.liter_pint_meters)
        self.cans_total = (self.total_liters / self.can_liters)
        self.pinch_money = (self.cans_total * self.can_liters_money)

        print(f'Quantidades de latas: {round(self.cans_total, 0)}')
        print(f'Preço total: R$ {round(self.pinch_money, 2)}')


paint_store = PaintStore()
paint_store.calc_quantities_cans()
