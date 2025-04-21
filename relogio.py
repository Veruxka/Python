import time
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    
    print(time.strftime("%H:%M:%S")) 
    
    time.sleep(1)