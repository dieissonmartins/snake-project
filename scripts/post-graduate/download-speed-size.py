"""
 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
 , calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""


class DownloadSpeedSize:

    def __init__(self):
        self.size = float(0.00)
        self.speed = float(0.00)
        self.time = float(0.00)

    def calc_time_download(self):
        self.size = float(input('Tamanho do arquivo (MB): '))
        self.speed = float(input('Velocidade de Internet (MBps): '))

        self.time = float((self.size / self.speed) * 60)

        print(f'Tempo aproximado de download: {self.time} Minutos')


time_download = DownloadSpeedSize()
time_download.calc_time_download()
