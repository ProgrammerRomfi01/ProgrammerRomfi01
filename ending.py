from tqdm import tqdm
from time import sleep

def ending():
    print('\n[------------Завершение!------------]')
    sleep(1.5)
    for i in tqdm(range(100), ncols=80, ascii=True):
        sleep(0.001)
    print('==========Спасибо что использовали на сервис!==========')

