import pandas as pd
import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))
import constants
from func.optimal_points import optimal_points
from func.graphs_2d_w import graphs_2d_w
from func.graph_3d_W_F import graph_3d_W_F
from func.general_graphs import general_graphs
from func.general_graphs_without_characteristics import general_graphs_without_characteristics
from func.general_graph_mx import general_graph_mx
from func.general_graph_fx import general_graph_fx


name_legend = constants.NAME_LEGEND
Mx_max = constants.MX_MAX
R_max = constants.R_MAX


"""Импорт таблиц с интерполированными данными"""

df_1 = pd.read_csv(os.path.abspath('Т1, серия 1 - инт 1.csv').replace('\\', '/'),
                    sep = ',').iloc[:,1:]
df_2 = pd.read_csv(os.path.abspath('Т1, серия 2 - инт 1.csv').replace('\\', '/'),
                    sep = ',').iloc[:,1:]

# Совместим результаты и  берём повторы
df_int = pd.concat([df_1, df_2], ignore_index=True).drop_duplicates(subset=constants.COLUMNS_AFTER_TRANSITION[:5]).reset_index(drop=True) 

"""Поиск оптимальных точек"""

df_for_2d, counter_W, W_min_for_counter, Vx_for_counter = optimal_points(df_int)
df_for_3d = optimal_points(df_int, full = "3d")
df_optimal = optimal_points(df_int, full = "optimal")




"""Графическое отображение"""

# 1. 2D График W сум
graphs_2d_w(df_for_2d, counter_W, W_min_for_counter, Vx_for_counter)

# 2. 3D График W сум и Fx от Vн, сохраняем вручную
graph_3d_W_F(df_for_3d).show()

# 3. Общий график
general_graphs(df_optimal, df_int)

# 3. Общий график без характеристик
general_graphs_without_characteristics(df_optimal, df_int, counter_W, W_min_for_counter, Vx_for_counter)

# 4. График моментов
general_graph_mx(df_optimal, df_int)

# 5. Грфик сил
general_graph_fx(df_optimal, df_int)