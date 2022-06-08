"""
 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês.
"""


class MonthlySalary:

    def __init__(self):
        self.earn_per_hour = 0
        self.hours_worked_month = 0

    def set_hours_worked_month(self):
        self.hours_worked_month = input('Quanto você ganha por hora \n')

    def set_earn_per_hour(self):
        self.earn_per_hour = input('Número de horas trabalhadas no mês \n')

    def calc_total_salary_month(self):
        per_hour = int(self.earn_per_hour)
        worked_month = int(self.hours_worked_month)

        total_salary_month = (per_hour * worked_month)

        print(f'Total do seu salário no referido mês é: R$ {total_salary_month} \n')


monthly_salary = MonthlySalary()
monthly_salary.set_hours_worked_month()
monthly_salary.set_earn_per_hour()
monthly_salary.calc_total_salary_month()
