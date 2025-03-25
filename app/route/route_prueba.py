from flask import Flask, render_template

import pymysql

# Se crea la instancia de la clase Flask
app = Flask(__name__)

try: 
    print("Intentando conectar con la base de datos")
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="hospital",
        port=3302
    )
    print("Conexión existosa con la base de datos.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")

@app.route('/')
def mostrar_pacientes():
    cursor = db.cursor()
    cursor.execute("SELECT nombre FROM paciente")
    paciente = cursor.fetchall()
    cursor.close()
    return render_template('example.html', vble_pacientes=paciente)

if __name__ == '__main__': 
    app.run(debug=True)