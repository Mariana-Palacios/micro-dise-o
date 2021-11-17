from flask import Flask, render_template, request, url_for
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='25bc741c9b5d0fff1d69f1281da69b31'

#@app.route("/", methods=['GET', 'POST'])
@app.route('/')
def home():
    form = LoginForm()
    return render_template('inicioSesion.html', title='Sign In', form=form)

@app.route("/registro")
def registro():
    form= FormularioRegistro()
    return render_template('registro.html',title='registro', form='form')

if __name__=="__main__":
    app.run(debug=True)