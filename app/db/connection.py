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
def validation_login(user, password):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM doctor WHERE dni = '{user}' AND contrasenya = '{password}'")
    result = cursor.fetchone()
    cursor.close()
    if result:
        print("Usuario encontrado en la base de datos")
        return result
    else:
        print("Usuario no encontrado en la base de datos")
        return None

# Listar pacientes según doctor
def getAllPatientsByDoctor(doctorDNI):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM paciente WHERE doctor_asignado = '{doctorDNI}' ORDER BY gravedad_ingreso DESC")
    pacientes = cursor.fetchall()
    cursor.close()
    return pacientes

def getPatientsByDNI(searchDNI, doctorDNI):
    cursor = db.cursor()
    try:
        cursor.execute(f"SELECT * FROM paciente WHERE doctor_asignado = '{doctorDNI}' AND dni LIKE '%{searchDNI}%' ORDER BY gravedad_ingreso DESC")        
        pacientes = cursor.fetchall()
    except Exception as e:
        print(f"Error en la consulta de búsqueda: {e}")
        pacientes = [] 
    finally:
        cursor.close()
    return pacientes

def getDataDoctor(doctorDNI):
    cursor = db.cursor()
    cursor.execute(f"SELECT nombre, especialidad FROM doctor WHERE dni = '{doctorDNI}'")
    nombre_doctor, especialidad = cursor.fetchone()
    cursor.close()
    return nombre_doctor, especialidad

# Búsqueda de paciente según su DNI
def getPatientByDNI(pacienteDNI):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM paciente WHERE dni = '{pacienteDNI}' ORDER BY gravedad_ingreso DESC")
    paciente = cursor.fetchone()
    cursor.close()
    return paciente

# Búsqueda de pacientes según doctor y motivo de ingreso
def getPatientsByDoctorAndIllness(doctorDNI, illnessLike):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM paciente WHERE doctor_asignado = '{doctorDNI}' AND motivo_ingreso LIKE '%{illnessLike}%'")
    pacientes = cursor.fetchall()
    cursor.close()
    return pacientes

# Eliminar paciente según DNI
def deletePatient(patientDNI):
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM paciente WHERE dni = '{patientDNI}'")
    db.commit()
    cursor.close()
