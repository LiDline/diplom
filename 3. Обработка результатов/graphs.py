from numpy import array, arange
from datetime import date
import pandas as pd
import plotly.graph_objects as go
import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))
import constants
from func.optimal_points import optimal_points
from func.graphs_2d_w import graphs_2d_w


name_legend = constants.NAME_LEGEND
Mx_max = constants.MX_MAX
R_max = constants.R_MAX


"""Импорт таблиц с интерполированными данными"""

df_1 = pd.read_csv(os.path.abspath('Т1, серия 1 - инт.csv').replace('\\', '/'),
                    sep = ',').iloc[:,1:]
df_2 = pd.read_csv(os.path.abspath('Т1, серия 2 - инт.csv').replace('\\', '/'),
                    sep = ',').iloc[:,1:]

# Совместим результаты и  берём повторы
df_int = pd.concat([df_1, df_2], ignore_index=True).drop_duplicates(subset=constants.COLUMNS_AFTER_TRANSITION[:5]).reset_index(drop=True) 

"""Поиск оптимальных точек"""

df_not_optimal, counter_W, W_min_for_counter, Vx_for_counter = optimal_points(df_int)
df_optimal = optimal_points(df_int, full = True)

# Vx = array(df.loc[:, 'Vн [км/ч]'].values)
# W_sum = array(df.loc[:, 'W сум [Вт]'].values)
# n1 = array(df.loc[:, 'n1 [об/мин]'].values)
# n2 = array(df.loc[:, 'n2 [об/мин]'].values)
# h1 = array(df.loc[:, 'h1 [град]'].values)
# h2 = array(df.loc[:, 'h2 [град]'].values)
# Mx1 = array(df.loc[:, 'Mвx1 [Н*м]'].values)
# Mx2 = array(df.loc[:, 'Mвx2 [Н*м]'].values)


"""Графическое отображение"""

# 1. 2D График W сум
graphs_2d_w(df_not_optimal, counter_W, W_min_for_counter, Vx_for_counter)