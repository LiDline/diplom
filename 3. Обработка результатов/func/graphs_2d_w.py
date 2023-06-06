import plotly.graph_objects as go
import numpy as np
from datetime import date
import os


import constants


Mx_max = constants.MX_MAX
R_max = constants.R_MAX


def graphs_2d_w(df, counter_W, W_min_for_counter, Vx_for_counter):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x = np.array(df.loc[:, 'Vн [км/ч]'].values), 
                             y = np.array(df.loc[:, 'W сум [Вт]'].values), mode = 'markers', 
                             line=dict(color='royalblue', width=0.5)))

    fig.update_xaxes(title_text="Vн [км/ч]",tickvals = np.arange(0, df['Vн [км/ч]'].max() +1, 1))
    fig.update_yaxes(title_text="W сум [Вт]")

    fig.update_layout(autosize=False,width=1400,height=600,
        margin=dict(l=80, r=100,b=50,t=50,pad=4
            )
        )
    fig.update_layout(           #Позиционирование заголовка
                   title={
                   'text': f"W сум от Vн ({round(sum(counter_W))} точек); -{Mx_max} < Mx < {Mx_max}; -{R_max} < Fx < {R_max}; {date.today()}",
                   'y':0.97,
                   'x':0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'})

    for i in range (0,49):
        if counter_W[i] > 0:
            fig.add_annotation(x=Vx_for_counter[i],y= W_min_for_counter[i],xref="x",yref="y",text=round(counter_W[i]),
                               font=dict(family="Times New Roman",size=18,color="black"),ax=5,ay=-25,)
    path = os.path.abspath("Изображения").replace("\\", "/")
    fig.write_image(f'{path}/3. W сум от Vн.png')        
