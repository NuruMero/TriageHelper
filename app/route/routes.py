from app import app
from flask import Flask, render_template, request, redirect, url_for
from app.db import connection
import app.constants as constants

# TODO Inicia sesión (datos de prueba)
user = connection.validation_login(constants.usernamePrueba, constants.passwordPrueba)[0]

# def logout():
    # user = None
    # return

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        dni = request.form['username']
        password = request.form['password']
        print("Recibidos datos del formulario")
        print(f"Usuario: {dni}, Contraseña: {password}")
        
        # Validacion credenciales
        result = connection.validation_login(dni, password)
        if result:
            print("Login exitoso, redirigiendo a index")
            return redirect(url_for('index'))
        else:
            print("Credenciales incorrectas")
            return "Credenciales incorrectas, intenta de nuevo"
        
    print("Mostrando pantalla de login")
    return render_template("login1.html")
    
# Rutas de API generales
@app.before_request
def before():
    print(f"CURRENT ROUTE => {request.url_rule}")

@app.errorhandler(404)
def notFound(e):
    return render_template("404.html", PageTitle="Page Not Found")

@app.route("/")
def index():
    print(app.url_map)
    pacientes = connection.getAllPatientsByDoctor(user[0])
    return render_template('example2.html', PageTitle="TriageHelper", vble_pacientes=pacientes)


# Rutas de la API de usuarios

@app.route('/pacientes')
def mostrar_pacientes():
    pacientes = connection.getAllPatientsByDoctor(user[0])
    return render_template('example.html', vble_pacientes=pacientes)