import plotly.graph_objects as go
import numpy as np
from datetime import date


import constants


Mx_max = constants.MX_MAX

def graph_3d_W_F(df_optimal):
    P1 =np.array(df_optimal.loc[:, 'Vн [км/ч]'].values)
    P2 = np.array(df_optimal.loc[:, 'W сум [Вт]'].values)
    P3 = np.array(df_optimal.loc[:, 'R сум [Н]'].values)
    x_plane = [0, 27, 27, 0, 0]
    y_plane = [-100, -100, 25000, 25000,-100]

    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=P1[0:], y=P2[0:], z=P3[0:], showlegend=False, mode='markers'))
    fig.update_traces(marker_size = 2)
    # Плоскость Mx = 0

    fig.add_trace(go.Scatter3d(x=x_plane,
                           y=y_plane,
                           z=[0, 0, 0, 0, 0], showlegend=False, surfaceaxis=2,
                           opacity=0.3, legendgroup="group2",
                           marker=dict(size=1, color='yellow', colorscale='Viridis',)))
    fig.add_trace(go.Scatter3d(x=x_plane,
                           y=y_plane,
                           z=[0, 0, 0, 0, 0], showlegend=False, surfaceaxis=-1,
                           opacity=0.3, legendgroup="group2",
                           marker=dict(size=1, color='black', colorscale='Viridis',))) 
                                                    # Оформленпе
#__________________________________________________________________________________________________________________
    
    tickf = 12
    fig.update_layout(autosize=False,
                  scene = {"aspectratio": {"x": 1, "y": 1, "z": 1},  #Масштаб осей
                  'camera_eye': {"x": -1, "y": -1, "z": 1},
                'camera_center' : {"x": 0, "y": 0, "z":0},}, 
                  width=950, height=500, #Размеры окна
                  margin=dict(l=10, r=0, b=10, t=50),
                 )
# Vн [км/ч] R сум [Н] Mx сум [Н*м]
    fig.update_layout(scene=dict(xaxis=dict(backgroundcolor="rgb(200, 200, 230)", title="Vн [км/ч]",
                         gridcolor="white",
                         showbackground=True,
                         zerolinecolor="white", tickfont=dict(size=tickf)),
    yaxis=dict(title="Wв [Вт]", 
                        backgroundcolor="rgb(230, 200,230)",
                        gridcolor="white",
                        showbackground=True,tickfont=dict(size=tickf),
                        zerolinecolor="white"),
    zaxis=dict(title="R сум [Н]",
               backgroundcolor="rgb(200, 200,200)",
                         gridcolor="white",
                         showbackground=True,tickfont=dict(size=tickf),
                         zerolinecolor="white")),
                 )
    fig.update_layout(           #Позиционирование заголовка
           title={
           'text': f"Характеристики сил и мощности от Vн для «Т1» ({round(len(P1))} точек); -{Mx_max} < Mx < {Mx_max}; {date.today()}",
           'y':0.97,
           'x':0.5,
           'xanchor': 'center',
           'yanchor': 'top'})     
    fig.update_layout(autosize=False,width=1400,height=600,
    margin=dict(l=50, r=50,b=50,t=50,pad=4
        )
    )
       

    fig.update_layout(scene=dict(xaxis_showspikes=False, yaxis_showspikes=False),) #Изменение при наведении мышки
    fig.update_scenes(camera_projection_type="orthographic") #вводит ортогональный вид
    return fig