import numpy as np
from scipy import interpolate
from datetime import date
import pandas as pd
import plotly.graph_objects as go
import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
import constants


# Т.к. расчёт аппарата был выполнен на упрощённой модели, подготовим значения сопротивления пловца.
def r_swimmer(graph=None):
    file = (os.path.abspath(f'1. Расчёты/1.2 Результаты расчётов/Доп. расчёты/Обдув реального аппарата.csv')).replace('\\', '/')
    df_real_apparat = pd.read_csv(file, sep = ',', skiprows=3)
    df_real_apparat =df_real_apparat.apply(pd.to_numeric, errors = 'coerce')
    df_real_apparat = pd.DataFrame(df_real_apparat.iloc[:,1:3])
    df_real_apparat.rename({'P8': f'{constants.COLUMNS_AFTER_TRANSITION[0]}',
                       'P9': f'{constants.COLUMNS_AFTER_TRANSITION[10]}'}, axis=1, inplace=True)
    
    # Интерполируем, а затем экстраполируем результаты обдува реального аппарата до 28 [км/ч] 
    f1_real_apparat = interpolate.interp1d(np.array(df_real_apparat.loc[:, f'{constants.COLUMNS_AFTER_TRANSITION[0]}'].values),
                         np.array(df_real_apparat.loc[:,f'{constants.COLUMNS_AFTER_TRANSITION[10]}'].values), 
                         kind = 'cubic')
    f2_real_apparat = np.poly1d(np.polyfit(np.arange(0, 20.5, 0.5), 
                                           f1_real_apparat(np.arange(0, 20.5, 0.5)), 
                                           3))
    R_real_apparat = f2_real_apparat(np.arange(20.5, 28, 0.5))


    # Сделаем тоже самое для расчётной модели
    df_model = pd.read_csv((os.path.abspath(f'1. Расчёты/1.2 Результаты расчётов/Доп. расчёты/Обдув модели.csv')).replace('\\', '/'),
                            sep = ',', skiprows=3)
    df_model = df_model.apply(pd.to_numeric, errors = 'coerce')
    df_model = pd.DataFrame(df_model.iloc[:,1:])
    df_model.rename({'P1': f'{constants.COLUMNS_AFTER_TRANSITION[0]}',
                       'P2': f'{constants.COLUMNS_AFTER_TRANSITION[10]}'}, axis=1, inplace=True)

    f1_model = interpolate.interp1d(np.array(df_model.loc[:, f'{constants.COLUMNS_AFTER_TRANSITION[0]}'].values),
                         np.array(df_model.loc[:, f'{constants.COLUMNS_AFTER_TRANSITION[10]}'].values), kind = 'cubic')
    
    f2_model = np.poly1d(np.polyfit(np.arange(0, 20.5, 0.5),
                                            f1_model(np.arange(0, 20.5, 0.5)),
                                            3))
    
    R_model = f2_model(np.arange(20.5, 28, 0.5))
    r_start = f1_real_apparat(np.arange(0, 20.5, 0.5)) - f1_model(np.arange(0, 20.5, 0.5))

    df_done = pd.DataFrame(columns = [f'{constants.COLUMNS_AFTER_TRANSITION[0]}', 
                                     f'{constants.COLUMNS_AFTER_TRANSITION[10]}'])
    df_done[f'{constants.COLUMNS_AFTER_TRANSITION[0]}'] = np.arange(0, 28, 0.5)
    df_done[f'{constants.COLUMNS_AFTER_TRANSITION[10]}'] = np.append(r_start, R_real_apparat - R_model)

    # Для графиков
    if graph:
        # 1-ый
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = np.arange(20, 28, 0.5),
                         y = f2_real_apparat(np.arange(20, 28, 0.5)),  mode='markers', 
                         marker =dict(color = 'black', size = 6), name = 'Экстр. точки'))                         
        fig.add_trace(go.Scatter(x = np.array(df_real_apparat.loc[:, 'Vн [км/ч]'].values),
                         y =np.array(df_real_apparat.loc[:, f'{constants.COLUMNS_AFTER_TRANSITION[10]}'].values), 
                         line=dict(color='royalblue', width=3), name = 'Расчётные точки'))                     


        fig.update_layout(autosize=False,width=1200,height=500,margin=dict(l=50, r=50,b=50,t=50,pad=4))      
        fig.update_layout(           #Позиционирование заголовка
                   title={
                   'text': f"Зависимость R аппарата от Vн; {date.today()}",
                   'y':0.97,
                   'x':0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'})
        fig.update_xaxes(title_text="Vн [км/ч]",tickvals = np.arange(0,30,1))
        fig.update_yaxes(title_text="R [Н]")

        path = os.path.abspath("Изображения").replace("\\", "/")
        fig.write_image(f'{path}/1. Сопротивление аппарата, экстр. значения.png')

        # 2-ой
        fig = go.Figure()  
        fig.add_trace(go.Scatter(x = np.arange(0, 28, 0.5),
                                 y = np.append(f1_real_apparat(np.arange(0, 20.5, 0.5)), R_real_apparat),
                                   line=dict(color='red', width=3), name = 'Аппарат'))   
        fig.add_trace(go.Scatter(x = np.arange(0, 28, 0.5),
                                 y = np.append(f1_real_apparat(np.arange(0, 20.5, 0.5)) - f2_model(np.arange(0, 20.5, 0.5)),
                                                R_real_apparat - R_model), 
                                 line=dict(color='black',dash = 'dot', width=3), name = 'Аппарат-T1'))                                       
        fig.add_trace(go.Scatter(x = np.arange(0, 28, 0.5),
                                 y = np.append(f1_model(np.arange(0, 20.5, 0.5)), R_model), 
                                 line=dict(color='royalblue', width=3), name = 'Т1'))

        fig.update_layout(autosize=False,width=1200,height=500,margin=dict(l=50, r=50,b=50,t=50,pad=4))      

        fig.update_xaxes(title_text="Vн [км/ч]",tickvals = np.arange(0,30,1))
        fig.update_yaxes(title_text="R [Н]",tickvals = np.arange(-2000,100,200))

        fig.update_layout(           #Позиционирование заголовка
                   title={
                   'text': f"Разница R пловца от Vн; {date.today()}",
                   'y':0.97,
                   'x':0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'})

        fig.write_image(f'{path}/2. Разница в сопротивлении моделей.png')    


    return df_done

