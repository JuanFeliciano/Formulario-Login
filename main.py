from flask import Flask,render_template,request,flash,redirect
import json

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'palavra-secreta123'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    with open('usuarios.json') as usuarios:
        lista = json.load(usuarios)
        cont = 0
        for c in lista:
            cont+=1
            if usuario == c['nome'] and ['senha'] == c['senha']:
                return render_template('acesso.html', nomeUsuario=c['nome'])
            if cont >= len(lista):
                flash('Usuario Inválido')
                return redirect('/')


@app.route('/css/login.css')
def css():
    return app.send_static_file('css/login.css')



if __name__ in '__main__': 
    app.run(debug=True)