from flask import Flask, render_template, request, url_for
from formularios import FormularioRegistro, InicioSesionFormulario

app = Flask(__name__)

app.config['SECRET_KEY']='25bc741c9b5d0fff1d69f1281da69b31'

@app.route("/")
def home():
    form= InicioSesionFormulario()
    return render_template("inicioSesion.html", form='form')

@app.route("/registro")
def registro():
    formulario= FormularioRegistro()
    return render_template('registro.html',title='registro', form='form')

if __name__=="__main__":
    app.run(debug=True)