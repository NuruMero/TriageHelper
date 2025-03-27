from app import app
from flask import Flask, render_template, request, redirect, url_for
from app.db import connection
import app.constants as constants

# TODO Inicia sesión (datos de prueba)
user = None

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global user 
    user = None
    return redirect(url_for('index'))
    
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
    global user
    print(user)
    if (user == None):
        return render_template('login1.html')
    else:
        paciente_search = request.args.get('search', '')
        if paciente_search:
            pacientes = connection.getPatientsByDNI(paciente_search, user[0])
        else:    
            pacientes = connection.getAllPatientsByDoctor(user[0])
        print(pacientes)
        nombre_doctor, especialidad = connection.getDataDoctor(user[0])
        return render_template('index.html', PageTitle="TriageHelper", vble_pacientes=pacientes, nombre_doctor=nombre_doctor, especialidad=especialidad)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        dni = request.form['username']
        password = request.form['password']
        
        # Validacion credenciales
        result = connection.validation_login(dni, password)
        if result:
            global user
            user = result
            return redirect(url_for('index'))
        else:
            print("Credenciales incorrectas")
            return render_template('login1.html', errorMsg="Credenciales incorrectas")
        
    print("Mostrando pantalla de login")
    return render_template("login1.html")

# Rutas de la API de usuarios