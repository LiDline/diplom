from numpy import array
import plotly.graph_objects as go
import numpy as np
from datetime import date
import os


import constants


Mx_max = constants.MX_MAX
R_max = constants.R_MAX
name_legend = constants.NAME_LEGEND



def general_graph_mx(df, df_int):
    Vx = array(df.loc[:, 'Vн [км/ч]'].values)

    fig = go.Figure()
                            # W1,2
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Wв1 [Вт]'].values), line=dict(color='royalblue', width=2), mode = 'markers+lines',name = name_legend[11]))
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Wв2 [Вт]'].values), line=dict(color='royalblue', width=2,dash='dot'), mode = 'markers+lines',name = name_legend[12]))

    fig.add_trace(go.Scatter(x = Vx, y = -np.array(df.loc[:, 'Mвx1 [Н*м]'].values), line=dict(color='black', width=2,dash='dash'), mode = 'markers+lines',
                             marker=dict(size=8,symbol = '150'),name = name_legend[5],yaxis="y2"))
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Mвx2 [Н*м]'].values), line=dict(color='brown', width=2), mode = 'markers+lines',
                             marker=dict(size=8,symbol = '150'),name = name_legend[6],yaxis="y2")) 
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Mкx [Н*м]'].values), line=dict(color='orange', width=2), mode = 'markers+lines',
                             marker=dict(size=8,symbol = 'x'),name = name_legend[13],yaxis="y2")) 
                                                            # Оси
    fig.update_layout(
        xaxis=dict(
            domain=[0.05, 0.93]),
        yaxis=dict(range=[-1150,11500],
            title="W сум [Вт]",tickvals = np.arange(0,12500,1150),), 
        yaxis2=dict(title="Mx [Н*м]",range=[-6.5,65],showgrid=False,tickvals = np.arange(-6.5,66.5,6.5),
            anchor="free",
            overlaying="y",
            side="right",
            position=0.935),
            )  


    fig.update_layout(legend=dict(
        yanchor="top", y=0.9, xanchor="left", x=0.2))

    fig.update_layout(autosize=False,width=1400,height=600,
        margin=dict(l=50, r=50,b=50,t=50,pad=4
            )
        )

    fig.update_layout(           #Позиционирование заголовка
               title={
               'text': f"Характеристики моментов и мощности от Vн для «Т1» (Всего {round((len(np.array(df_int.loc[:, 'Vн [км/ч]'].values))/1000000),2)} млн инт. точек); -{Mx_max} < Mx < {Mx_max}, -{R_max} < Fx < {R_max}; {date.today()}",
               'y':0.97, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})

    fig.update_xaxes(title_text="Vн [км/ч]",tickvals = np.arange(0, df['Vн [км/ч]'].max() +1, 1))   

    path = os.path.abspath("Изображения").replace("\\", "/")
    fig.write_image(f'{path}/6. Mx и W от Vн для Т1.png')    