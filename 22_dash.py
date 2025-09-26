import dash
from dash import dcc, html 
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div([
    html.H1("Grafico interativo com Dash"),
    dcc.Graph(
        id = 'grafico-1',
        figure = {
            'data':[
                go.Scatter(
                    x = [1, 2, 3, 4, 5],
                    y = [10, 11, 12, 13, 14],
                    mode = 'lines+markers',
                    name = 'Linha 1'
                    ),
                ],
                'layout':go.Layout(
                    title = "Grafico de Linha Interativa",
                    xaxis = {'title': 'Eixo X'},
                    yaxis = {'title': 'Eixo Y'}
            )
        }
    )
])
if __name__ == '__main__':
    app.run(debug=True)