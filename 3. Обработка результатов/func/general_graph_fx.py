from numpy import array
import plotly.graph_objects as go
import numpy as np
from datetime import date
import os


import constants


Mx_max = constants.MX_MAX
R_max = constants.R_MAX
name_legend = constants.NAME_LEGEND

def general_graph_fx(df, df_int):
    Vx = array(df.loc[:, 'Vн [км/ч]'].values)
    fig = go.Figure()
                        # W1,2
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Wв1 [Вт]'].values), line=dict(color='royalblue', width=2), mode = 'markers+lines',name = name_legend[11]))
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Wв2 [Вт]'].values), line=dict(color='royalblue', width=2,dash='dot'), mode = 'markers+lines',name = name_legend[12]))
                            # RВ1,2
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Тв1 [Н]'].values), line=dict(color='teal', width=2,dash='dashdot'), mode = 'markers+lines',
                             marker=dict(size=8,symbol = 'arrow-bar-up-open'),name = name_legend[7],yaxis="y2"))   
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Тв2 [Н]'].values), line=dict(color='turquoise', width=2,dash='dashdot'), mode = 'markers+lines',
                             marker=dict(size=8,symbol = 'arrow-bar-up-open'),name = name_legend[8],yaxis="y2")) 
                            #RК1,2
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Rк1 [Н]'].values), line=dict(color='green', width=1,dash='dot'), mode = 'markers+lines',
                             marker=dict(size=8,symbol = '152'),name = name_legend[9],yaxis="y2"))  
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'Rк2 [Н]'].values), line=dict(color='tan', width=1,dash='dot'), mode = 'markers+lines',
                             marker=dict(size=8,symbol = '152'),name = name_legend[10],yaxis="y2")) 
                             #R тела
    fig.add_trace(go.Scatter(x = Vx, y = -np.array(df.loc[:, 'R тела [Н]'].values), line=dict(color='red', width=2), mode = 'markers+lines',
                             marker=dict(size=8,symbol = 'x'),name = name_legend[14],yaxis="y2"))                            
                            #R ВМГ
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'R ВМГ [Н]'].values), line=dict(color='orange', width=2), mode = 'markers+lines',
                             marker=dict(size=8,symbol = 'x'),name = name_legend[15],yaxis="y2"))   
    fig.add_trace(go.Scatter(x = Vx, y = np.array(df.loc[:, 'R сум [Н]'].values), line=dict(color='black', width=1), mode = 'markers+lines',
                             marker=dict(size=5),name = name_legend[16],yaxis="y2")) 
    
    
                                                            # Оси
    fig.update_layout(
        xaxis=dict(
            domain=[0.05, 0.93]),
        yaxis=dict(range=[0,11500],tickvals = np.arange(0,12500,1150),
            title="W сум [Вт]"), 
        yaxis2=dict(title="R [Н]",range=[-130,1700],showgrid=False,tickvals = np.arange(-130,1883,183),
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
               'text': f"Характеристики сил и мощности от Vн для «Т1» (Всего {round((len(np.array(df_int.loc[:, 'Vн [км/ч]'].values))/1000000),2)} млн инт. точек); -{Mx_max} < Mx < {Mx_max}, -{R_max} < Fx < {R_max}; {date.today()}",
               'y':0.97, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
    
    fig.update_xaxes(title_text="Vн [км/ч]",tickvals = np.arange(0, df['Vн [км/ч]'].max() +1, 1))
    path = os.path.abspath("Изображения").replace("\\", "/")
    fig.write_image(f'{path}/7. R и W от Vн для Т1.png')   
 