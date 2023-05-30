import os
import pandas as pd


import constants


columns = constants.COLUMNS_AFTER_CALCULATIONS

# Пройдёмся по всем .csv и "склеим" их
def union_results(series, number = 49):

    if series == 1:
        number = 25
    
    df = pd.DataFrame(columns = columns)

    for i in range(number):
        file = (os.path.abspath(f'1. Расчёты/1.2 Результаты расчётов/М1/{series}-ая серия/{i+1}.csv')).replace('\\', '/')
        new_df = pd.read_csv(file, sep = ',', skiprows=3).iloc[:,1:]
        new_df.columns = columns    # Иначе не соединятся
        new_df = new_df.apply(pd.to_numeric, errors = 'coerce')

        df = pd.concat([df, new_df], ignore_index=True)

    return df.drop_duplicates().reset_index(drop=True)    