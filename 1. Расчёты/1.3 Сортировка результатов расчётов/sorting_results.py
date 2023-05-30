import sys
import os


# Определяем абсолютный путь к файлу constants.py
constants_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'constants.py')
# Добавляем путь в sys.path
sys.path.append(constants_path)
print(constants_path)
from func.iterating_results import iterating_results


def sorting_results():

    '''1. Импортируем нужные файлы и создадим из них одну таблицу'''

    df_1 = iterating_results(1)
    df_2 = iterating_results(2)
    
    print(df_1)   

    

sorting_results()    