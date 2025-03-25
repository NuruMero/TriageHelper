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
def login(credentials):
    cursor = db.cursor()
    cursor.execute(f"SELECT dni FROM doctor WHERE dni = '{credentials.dni}' AND WHERE contrasenya = {credentials.password()}")
    result = cursor.fetchall()
    cursor.close()
    if result:
        return result
    else:
        return None
    
# Listar pacientes
def getAllPatients():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM paciente")
    pacientes = cursor.fetchall()
    cursor.close()
    return pacientes