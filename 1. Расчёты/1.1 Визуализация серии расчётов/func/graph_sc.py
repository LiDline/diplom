import plotly.graph_objects as go

def graph_sc(fig, i, matrix, name):
    fig.add_trace(go.Scatter3d(x = [matrix[0][3]],
                            y = [matrix[1][3]],
                            z = [matrix[2][3]],
                            showlegend=True, name = name, opacity=1, legendgroup=f"group{i}", marker=dict(size=6, color='gray', colorscale='Viridis')))

    fig.add_trace(go.Scatter3d(x = [matrix[0][3], matrix[0][0]],
                                y = [matrix[1][3], matrix[1][0]],
                                z = [matrix[2][3], matrix[2][0]],
                showlegend=False, opacity=1, legendgroup=f"group{i}", marker=dict(size=1, color='red', colorscale='Viridis',), line = dict(width = 7))) 
    fig.add_trace(go.Scatter3d(x = [matrix[0][3], matrix[0][1]],
                                y = [matrix[1][3], matrix[1][1]],
                                z = [matrix[2][3], matrix[2][1]],
                showlegend=False, opacity=1, legendgroup=f"group{i}", marker=dict(size=1, color='green', colorscale='Viridis',), line = dict(width = 7))) 
    fig.add_trace(go.Scatter3d(x = [matrix[0][3], matrix[0][2]],
                                y = [matrix[1][3], matrix[1][2]],
                                z = [matrix[2][3], matrix[2][2]],
                showlegend=False, opacity=1, legendgroup=f"group{i}", marker=dict(size=1, color='blue', colorscale='Viridis',), line = dict(width = 7)))              