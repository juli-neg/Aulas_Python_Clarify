import plotly.graph_objs as go

eixo_x = [1, 2, 3, 4, 5]
eixo_y = [10, 11, 12, 13, 14]

# criando um grafico de linha
fig = go.Figure(
    data=go.Scatter(
        x = eixo_x,
        y = eixo_y,
        mode = 'lines+markers',
        name = 'Linha 1'
        )
    )
fig.update_layout(
    title = "Grafico de Linha Interativa",
    xaxis_title = "Unidades",
    yaxis_title = "Dezenas"
)

fig.show()