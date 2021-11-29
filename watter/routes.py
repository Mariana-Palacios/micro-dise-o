from watter import app, bcrypt, db
from watter.dbUsuario import Usuario, Post
from watter.forms import RegistroForm, InicioForm, PostForm
from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required


#@app.route("/", methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = InicioForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form.password.data):
            login_user(usuario, remember=form.remember.data)
        return redirect(url_for('post_form'))
    return render_template('inicioSesion.html', form=form)

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    form= RegistroForm()
    if form.validate_on_submit():
        hash_p = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        nuevoUsuario = Usuario(username=form.username.data, email=form.email.data, password=hash_p)
        db.session.add(nuevoUsuario)
        db.session.commit()
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
