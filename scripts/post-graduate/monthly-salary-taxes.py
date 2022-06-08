"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.

    calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.

"""


class MonthlySalaryTaxes:

    def __init__(self):
        self.earn_per_hour = 0
        self.hours_worked_month = 0

        self.gross_salary = 0
        self.net_salary = 0

        self.tax_inss = 0
        self.tax_syndicate = 0
        self.tax_ir = 0

    def set_hours_worked_month(self):
        self.hours_worked_month = input('Quanto você ganha por hora \n')

    def set_earn_per_hour(self):
        self.earn_per_hour = input('Número de horas trabalhadas no mês \n')

    def calc_total_salary_month(self):
        per_hour = int(self.earn_per_hour)
        worked_month = int(self.hours_worked_month)

        self.gross_salary = float(per_hour * worked_month)
        self.tax_inss = float(self.calculate_percentage(self.gross_salary, 8))
        self.tax_syndicate = float(self.calculate_percentage(self.gross_salary, 5))
        self.tax_ir = float(self.calculate_percentage(self.gross_salary, 11))
        self.net_salary = float(self.gross_salary - (self.tax_inss + self.tax_syndicate + self.tax_ir))

        print(f'+ Salário Bruto : R$ {self.gross_salary}')
        print(f'- IR (11%) : R$ {self.tax_ir}')
        print(f'- INSS (8%) : R$ {self.tax_inss}')
        print(f'- Sindicato (5%) : R$ {self.tax_syndicate}')
        print(f'= Salário Liquido : R$ {self.net_salary}')

    def calculate_percentage(self, value_total, percentage):

        discount_value = value_total * (percentage / 100)

        resp = discount_value

        return resp


monthly_salary = MonthlySalaryTaxes()
monthly_salary.set_hours_worked_month()
monthly_salary.set_earn_per_hour()
monthly_salary.calc_total_salary_month()
