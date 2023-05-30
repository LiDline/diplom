import pandas as pd
import plotly.graph_objects as go
from numpy import arange, array
from func.graph_sc import graph_sc
from func.graph_settings import graph_settings
from func.vizualise_of_serial import vizualise_of_serial


"""1-ая серия"""
h1_2_first_series = arange(20, 30 + 2.5, 2.5)
n1_2_first_series = arange(0, 1000 + 250, 250)
Vx1_2_first_series = arange(0, 12.5 + 2.5, 2.5)
l1 = (((max(h1_2_first_series) - min(h1_2_first_series))/2.5 + 1)**2 * ((max(n1_2_first_series) - min(n1_2_first_series))/250 + 1)** 2
    * ((max(Vx1_2_first_series) - min(Vx1_2_first_series))/2.5 + 1))

"""2-ая серия"""
h1_2_second_series = arange(20, 35 + 2.5, 2.5)
n1_2_second_series = arange(750, 1500 + 250, 250)
Vx1_2_second_series = arange(0, 27.5 + 2.5, 2.5)
l2 = (((max(h1_2_second_series) - min(h1_2_second_series))/2.5 + 1)**2 * ((max(n1_2_second_series) - min(n1_2_second_series))/250 + 1)** 2
    * ((max(Vx1_2_second_series) - min(Vx1_2_second_series))/2.5 + 1))

global_coordinate_system = array([[1500, 0, 0, 0],
                                [0, 35, 0, 0],
                                [0, 0, 27.5, 0]])

fig = go.Figure()

graph_sc(fig, 1, global_coordinate_system, 'Глобал. СК') # Отрисовка глоб. СК  

fig.add_trace(go.Scatter3d(x = [0], y = [0], z = [0],
                showlegend=False, surfaceaxis=0,  opacity=0, legendgroup="group2",
                marker=dict(size=1, color='red', colorscale='Viridis')))

"""1-ая серия"""
vizualise_of_serial(fig, n1_2_first_series, h1_2_first_series, Vx1_2_first_series, 1, 1, 'red', f'1-ая серия ({round(l1)})', 2)

"""2-ая серия"""
vizualise_of_serial(fig, n1_2_second_series, h1_2_second_series, Vx1_2_second_series, 1, 1, 'orange', f'2-ая серия ({round(l2)})', 3)

#___________________________________________________________________________________________________

"""Настройка отображения"""

graph_settings(fig, 1100, 700, "n1,2 [об/мин]", "h1,2 [об/мин]", "Vн [км/ч]", f'12 558 точек') # Цифры - размеры отображаемого окна

fig.show()     