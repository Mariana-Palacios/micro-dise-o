from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormularioRegistro(FlaskForm):
    usuario = StringField('Usuario', validators= [DataRequired(), Length(min=1, max=20)])
    correo = StringField('Email', validators= [DataRequired(),Email()])
    contrasena= PasswordField('Confirmar contraseña', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrate')

class InicioSesionFormulario(FlaskForm):
    correo = StringField('Correo', validators= [DataRequired(),Email()])
    contrasena = PasswordField('Contraseña',validators= [DataRequired(), EqualTo('password')])
    recuperarContrasena = BooleanField('Recuperar contraseña')
    submit = SubmitField('Entrar')