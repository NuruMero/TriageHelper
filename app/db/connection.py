# Archivo de conexión para la base de datos
import pymysql

try:
    print("Intentando conectar a la base de datos...")
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
    )
    print("Conexión exitosa con la base de datos.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")

# MÉTODOS DE ACCESO A DB

# Confirmar login
def login(user, password):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM doctor WHERE dni = '{user}' AND contrasenya = '{password}'")
    result = cursor.fetchall()
    cursor.close()
    if result:
        return result
    else:
        return None
    
# Listar pacientes
def getAllPatientsByDoctor(doctorDNI):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM paciente WHERE doctor_asignado = '{doctorDNI}'")
    pacientes = cursor.fetchall()
    cursor.close()
    return pacientes
