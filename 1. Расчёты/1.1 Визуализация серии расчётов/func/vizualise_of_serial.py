import plotly.graph_objects as go
from numpy import array

def vizualise_of_serial(fig, n, h, Vx, opacity_planes, opacity_lines, color, name, group):

    border_xyz = array([[min(n), min(n), min(n), min(n), min(n), max(n), max(n), min(n), max(n), max(n), min(n), min(n), max(n), max(n), max(n), max(n)], 
                    [min(h), max(h), max(h), min(h), min(h), min(h), min(h), min(h), min(h), max(h), max(h), max(h), max(h), max(h), max(h), min(h)],
                    [min(Vx), min(Vx), max(Vx), max(Vx), min(Vx), min(Vx), max(Vx), max(Vx), max(Vx), max(Vx), max(Vx), min(Vx), min(Vx), max(Vx), min(Vx), min(Vx)]])

    fig.add_trace(go.Scatter3d(x = [n[0]] * 4, y = [min(h), min(h), max(h), max(h)], 
                                z = [min(Vx), max(Vx),  max(Vx), min(Vx)],
                                showlegend=True, name = name, surfaceaxis=0,  opacity=opacity_planes, legendgroup=f"group{group}",
                                marker=dict(size=1, color=color, colorscale='Viridis')))
    fig.add_trace(go.Scatter3d(x = [max(n)] * 4,
                            y = [min(h), min(h), max(h), max(h)], 
                            z = [min(Vx), max(Vx),  max(Vx), min(Vx)],
                    showlegend=False, surfaceaxis=0,  opacity=opacity_planes, legendgroup=f"group{group}",
                    marker=dict(size=1, color=color, colorscale='Viridis')))
    fig.add_trace(go.Scatter3d(x = [min(n), max(n), max(n), min(n)], y = [h[0]] * 4 , 
                                z = [min(Vx), min(Vx), max(Vx),  max(Vx)],
                    showlegend=False, surfaceaxis=1,  opacity=opacity_planes, legendgroup=f"group{group}",
                    marker=dict(size=1, color=color, colorscale='Viridis')))
    fig.add_trace(go.Scatter3d(x = [min(n), max(n), max(n), min(n)], y = [max(h)] * 4 , 
                                z = [min(Vx), min(Vx), max(Vx),  max(Vx)],
                    showlegend=False, surfaceaxis=1,  opacity=opacity_planes, legendgroup=f"group{group}",
                    marker=dict(size=1, color=color, colorscale='Viridis')))
    fig.add_trace(go.Scatter3d(x = [max(n), max(n), min(n), min(n)],
                                y = [max(h), min(h), min(h), max(h)] ,    
                                z = [min(Vx)] * 4,
                    showlegend=False, surfaceaxis=2,  opacity=opacity_planes, legendgroup=f"group{group}",
                    marker=dict(size=1, color=color, colorscale='Viridis')))
    fig.add_trace(go.Scatter3d(x = [max(n), max(n), min(n), min(n)],
                                y = [max(h), min(h), min(h), max(h)] ,    
                                z = [max(Vx)] * 4,
                    showlegend=False, surfaceaxis=2,  opacity=opacity_planes, legendgroup=f"group{group}",
                    marker=dict(size=1, color=color, colorscale='Viridis')))                
    fig.add_trace(go.Scatter3d(x = border_xyz[0], y = border_xyz[1], z = border_xyz[2],   
                    showlegend=False, surfaceaxis=-1, opacity=opacity_lines, legendgroup=f"group{group}", marker=dict(size=1, color='black')))