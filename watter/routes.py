from watter import app, bcrypt, db
from watter.dbUsuario import Usuario, Post
from watter.forms import RegistroForm, InicioForm, PostForm
from flask import render_template, request, url_for, flash, redirect

#@app.route("/", methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = InicioForm()
    if request.method == 'POST':
        #name = request.form['name']
        #email = request.form['email']
        #password = request.form['password']
        return redirect(url_for('post_form'))
    return render_template('inicioSesion.html', form=form)

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    form= RegistroForm()
    if form.validate_on_submit():
        hash_p = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        nuevoUsuario = Usuario(nombre=form.usuario.data, email=form.email.data, password=hash_p)
        db.session.add(nuevoUsuario)
        db.session.commit()
        flash(f'{form.usuario.data}, ha sido registrado con exito!')
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