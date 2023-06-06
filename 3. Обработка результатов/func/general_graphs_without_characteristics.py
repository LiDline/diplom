from numpy import array
import plotly.graph_objects as go
import numpy as np
from datetime import date
import os


import constants


Mx_max = constants.MX_MAX
R_max = constants.R_MAX
name_legend = constants.NAME_LEGEND


def general_graphs_without_characteristics(df, df_int, counter_W, W_min_for_counter, Vx_for_counter):
    Vx = array(df.loc[:, 'Vн [км/ч]'].values)
    W_sum = array(df.loc[:, 'W сум [Вт]'].values)
    n1 = array(df.loc[:, 'n1 [об/мин]'].values)
    n2 = array(df.loc[:, 'n2 [об/мин]'].values)
    h1 = array(df.loc[:, 'h1 [град]'].values)
    h2 = array(df.loc[:, 'h2 [град]'].values)
    fig = go.Figure()           

    fig.add_trace(go.Scatter(x = Vx, y = W_sum, line=dict(color='royalblue', width=2), mode = 'markers+lines',xaxis = "x1",
                             name = name_legend[4]))

    fig.add_trace(go.Scatter(x = Vx, y = n1, line=dict(color='red', width=1), mode = 'markers+lines',
                                     marker=dict(size=8,symbol = 'triangle-right'),
                                     showlegend = True, name = name_legend[0],yaxis="y2"))
    fig.add_trace(go.Scatter(x = Vx, y = -n2, line=dict(color='black', width=1),mode = 'markers+lines',
                                     marker=dict(size=8,symbol = 'triangle-left'),showlegend = True, name = name_legend[1],yaxis="y2"))

    fig.add_trace(go.Scatter(x = Vx, y = h1, line=dict(color='orange', width=1),mode = 'markers+lines',
                             marker=dict(size=8,symbol = 'x-dot'),showlegend = True, name = name_legend[2],yaxis="y3"))
    fig.add_trace(go.Scatter(x = Vx, y = -h2, line=dict(color='green', width=1), mode = 'markers+lines',
                              marker=dict(size=8,symbol = 'x-dot'),showlegend = True, name = name_legend[3],yaxis="y3"))

    fig.add_trace(go.Scatter(x = [1,2], y = [1], mode = 'markers',marker=dict(size=8,color = '#ff7f0e'),marker_symbol = 'square', showlegend = True, name = "оптимальные интер. точки",yaxis="y3"))
    for i in range (0,55):
        if counter_W[i] > 0:
            fig.add_annotation(x=Vx_for_counter[i],y= W_min_for_counter[i],xref="x",yref="y",
                               text=int(counter_W[i]),font=dict(family="Times New Roman",size=12,color="white"),ax=0,ay=18,
            bordercolor="#c7c7c7",
            borderwidth=1,
            borderpad=4,
            bgcolor="#ff7f0e",
            opacity=0.8
            ) 
    #______________________________________
    fig.update_layout(
        xaxis=dict(
            domain=[0.03, 0.9]),
        yaxis=dict(range=[-1850,18500],
            title="W сум [Вт]", tickvals = np.arange(-1850,20350,1850),),
        yaxis2=dict(title="n [об/мин]",range=[-300,3000],showgrid=False,tickvals = np.arange(-300,3300,300),
            anchor="free",
            overlaying="y",
            side="right",
            position=0.91),
        yaxis3=dict(title="h [град]",range=[-3.5,35],showgrid=False,tickvals = np.arange(-3.5,38.5,3.5),
            anchor="free",
            overlaying="y",
            side="right",
            position=0.97), 
        yaxis4=dict()         
            )  

    fig.update_layout(legend=dict(
        yanchor="top", y=0.6, xanchor="left", x=0.2))

    fig.update_layout(autosize=False,width=1400,height=600,
        margin=dict(l=50, r=50,b=50,t=50,pad=4
            )
        )

    fig.update_layout(           #Позиционирование заголовка
               title={
               'text': f"Кол-во расчётных точек модели «Т1» (Всего {round((len(np.array(df_int.loc[:, 'Vн [км/ч]'].values))/1000000),2)} млн инт. точек); -{Mx_max} < Mx < {Mx_max}, -{R_max} < Fx < {R_max}; {date.today()}",
               'y':0.97, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
    fig.update_xaxes(title_text="Vн [км/ч]",tickvals = np.arange(0, df['Vн [км/ч]'].max() +1, 1))
    
    path = os.path.abspath("Изображения").replace("\\", "/")
    fig.write_image(f'{path}/5. Общие характеристики Т1 (без Fx и Mx).png')      