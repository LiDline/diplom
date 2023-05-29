from datetime import date

def graph_settings(fig, width, height, OX, OY, OZ, counter):

    fig.update_layout(title={'text': f"Диаграмма объёма расчётов ({counter}); {date.today()}",
                      'y':0.97,'x':0.5,'xanchor': 'center','yanchor': 'top'})
    
                                                 #Оформление
    fig.update_layout(legend=dict(yanchor="top", y=0.99,xanchor="left", x=0.8))
    
    tickf = 12
    fig.update_layout(autosize=True, scene = {'camera_eye': {"x": -2, "y": 2, "z":1.65},'camera_center' : {"x": -0.3, "y": 0, "z":0},},
                      width=width, height=height, margin=dict(l=10, r=0, b=10, t=50))
    
    fig.update_layout(scene=dict(xaxis=dict( title=OX,backgroundcolor="rgb(200, 200, 230)",gridcolor="white",
                             showbackground=True,zerolinecolor="white", tickfont=dict(size=tickf)),
                      yaxis=dict(title=OY, backgroundcolor="rgb(230, 200,230)",gridcolor="white",
                            showbackground=True,tickfont=dict(size=tickf),zerolinecolor="white"),
                      zaxis=dict(title= OZ, backgroundcolor="rgb(200, 200,200)",gridcolor="white",
                             showbackground=True,tickfont=dict(size=tickf),zerolinecolor="white",)))
    
    fig.update_layout(scene=dict(xaxis_showspikes=False, yaxis_showspikes=False),)
    fig.update_scenes(camera_projection_type="orthographic")  