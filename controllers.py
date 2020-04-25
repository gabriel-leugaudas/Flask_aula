from aplicacao import app
from flask import render_template

@app.route('/home')
def ola():
    return '<h1>Olá Mundo de Novo!</h1>'

@app.route('/')
def pagina_principal():
    return render_template('index.html')

@app.route('/outra')
def outra_pagina():
    return '<h1>Outra Pagina</h1>'

app.run(debug=True)