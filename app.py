from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistroForm, InicioForm, PostForm

app = Flask(__name__)

app.config['SECRET_KEY']='25bc741c9b5d0fff1d69f1281da69b31'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    imagen_perfil = db.Column(db.String(20), nullable=False, 'sin_imagen.jpg')

class Post(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.email}' )"

#@app.route("/", methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = InicioForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('post_form'))
    return render_template('inicioSesion.html', form=form)

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    form= RegistroForm()
    if form.validate_on_submit():
        flash(f'{form.username.data}, ha sido registrado con exito!')
        return redirect(url_for('post_form'))
    return render_template('registro.html', form=form)

@app.route("/grafica/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/grafica/<int:post_id>/", methods=['GET', 'POST'])
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data
        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)
        return redirect(url_for('post_form'))
    return render_template("graficas.html", form=form, title='grafica')

if __name__=="__main__":
    app.run(debug=True)