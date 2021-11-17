from flask import Flask, render_template, request, url_for
from forms import LoginForm, PostForm

app = Flask(__name__)

app.config['SECRET_KEY']='25bc741c9b5d0fff1d69f1281da69b31'

#@app.route("/", methods=['GET', 'POST'])
@app.route('/')
def home():
    form = LoginForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
    return render_template('inicioSesion.html', form=form)

@app.route("/registro")
def registro():
    form= FormularioRegistro()
    return render_template('registro.html',title='registro', form='form')

@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data
        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)
        return redirect(url_for('post_form'))
    return render_template("graficas.html", form=form, title='registro')

if __name__=="__main__":
    app.run(debug=True)