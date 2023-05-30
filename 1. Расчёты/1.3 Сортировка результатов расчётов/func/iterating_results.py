import os
import sys
import pandas as pd


# Определяем абсолютный путь к файлу constants.py
constants_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'constants.py')
# Добавляем путь в sys.path
sys.path.append(constants_path)
import constants


columns = constants.COLUMNS_AFTER_CALCULATIONS

# Пройдёмся по всем .csv и "склеим" их
def iterating_results(series, number = 49):

    

    if series == 1:
        number = 25

    
    df = pd.DataFrame(columns = columns)

    for i in range(number-1):
        file = (os.path.abspath(f'1. Расчёты/1.2 Результаты расчётов/М1/{series}-ая серия/{i+1}.csv')).replace('\\', '/')
        new_df = pd.read_csv(file, sep = ',', skiprows=3).iloc[:,1:]
        new_df.columns = columns    # Иначе не соединятся
        new_df = new_df.apply(pd.to_numeric, errors = 'coerce')

        df = pd.concat([df, new_df], ignore_index=True)

    return df    