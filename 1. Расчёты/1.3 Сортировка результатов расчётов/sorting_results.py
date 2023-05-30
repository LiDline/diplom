import sys
import os


# Определяем абсолютный путь к файлу constants.py
constants_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# Добавляем путь в sys.path
sys.path.insert(0, constants_path)
import constants
from func.union_results import union_results
from func.sorting import sorting



def sorting_results():

    '''1. Импортируем нужные файлы и создадим из них одну таблицу'''

    df_1 = union_results(1)
    df_2 = union_results(2)
    
    '''2. Пересортируем данные для дальнейшей интерполяции''' 

    df_1 = df_1.reindex(columns=constants.COLUMNS_AFTER_TRANSITION)
    df_2 = df_2.reindex(columns=constants.COLUMNS_AFTER_TRANSITION)

    df_1 = sorting(df_1)
    df_2 = sorting(df_2)
    
    return df_2

print(sorting_results())