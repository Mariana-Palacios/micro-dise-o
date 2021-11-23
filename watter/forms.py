from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from watter.dbUsuario import Usuario

class InicioForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    recuperar = BooleanField('Recuperar contaseña')
    submit = SubmitField('Iniciar Sesion')

class RegistroForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirmar_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registratse')

    def verificacion_usuario(self, usuario):
        user = User.query.filter_by(nombre=usuario.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    
    #verificar si el correo existe 
    def verificacion_email(self, email):

        correo = Usuario.query.filter_by(email=email.data).first()

        if correo:
            raise ValidationError('El correo, ya existe porfavor ingrese otro correo')

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')