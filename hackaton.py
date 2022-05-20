from time import sleep
from app import *

action = input('Введите действие (0 - остановить ввод):')
total_time = 0
dict_actions = dict()

def read_lists(lists):
    return 1800*lists/150/60

def new_lists(rest_time):
    return rest_time*60*150/1800

while action != '0':

    hours_start = int(input('Введите время начала действия в часах (от 10 до 24 часов):'))
    hours_end = int(input('Введите время конца действия в часах (от 10 до 24 часов):'))

    if hours_start < 10 or hours_end < 10:
        print('Это слишком мало для анализа и ввода. Пожалуйста повторите ввод!')
    elif hours_start > 24 or hours_end > 24:
        print('К сожалению в сутках 24 часа. Пожалуйста, проверьте данные и повторите запрос.')
    else:
        if hours_end < hours_start:
            print('Некорректный ввод.')
        else:
            dict_actions[action] = (hours_end - hours_start)
            total_time += (hours_end - hours_start)
    action = input('Введите действие (0 - остановить ввод):')

calculation()

print('Список дел:')
for act in dict_actions:
    print(act, '-', dict_actions[act], 'ч.')
    if dict_actions[act] > 3:
        print('Слишком много времени тратится на действие "' + act + '"! Это действие можно оптимизировать!')

print('Общее время (в часах):', total_time)

rest_time = 14 - total_time

if rest_time > 0:
    print('У вас осталось', rest_time, 'ч. Потратье это время на что-то полезное. Например, чтение научной или художественной литературы.')
    question = input('Вы любите читать? (да/нет)')
    if question == 'да':
        lists = int(input('Сколько страниц вы могли бы читать в день?'))
        read_lists = read_lists(lists)
        
        if read_lists <= rest_time:
            print('На чтение,', lists, 'стр. вам потребуется', int(round(read_lists, 0)), 'ч.')
        else:
            new_lists = new_lists(rest_time)
            
            print('К сожалению вы не успеете прочитать,', lists, 'стр. за', rest_time, 'ч. За это время вы успеете прочитать только', new_lists, 'стр.')
    else:
        print('Понятно')
else:
    print('У вас нет свободного времени. Нужно оптимизировать действия, чтобы у вас было свободное время на полезные дела!')

