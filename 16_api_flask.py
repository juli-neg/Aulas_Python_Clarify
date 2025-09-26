r"""
     _       _ _                   
    | |_   _| (_) __ _ _ __   __ _ 
 _  | | | | | | |/ _` | '_ \ / _` |
| |_| | |_| | | | (_| | | | | (_| |
 \___/ \__,_|_|_|\__,_|_| |_|\__,_|

 Autora: Juliana Negreiros
 Versão: 0.0.0.1
 Data: 25-09-2025
 """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return " <h1> Bem vindo a minha página </h1>    <a href='/sobre'> Sobre <a> <br> <a href='/saudacao/juliana'> Saudacao </a>"

@app.route('/sobre')
def informacoes():
    return "<marquee> Juliana Negreiros de Moura </marquee>"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"<h1>Bem vindo </h1>{nome}!"

if __name__ == '__main__':
    app .run(debug=True)