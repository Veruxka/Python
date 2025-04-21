import time
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela dependendo do sistema operacional
    print(time.strftime("%H:%M:%S"))  # Exibe o horário atual no formato hora:minuto:segundo
    time.sleep(1)