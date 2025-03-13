# Importamos las librerías necesarias
from flask import Flask, render_template, request, redirect  # Flask para la aplicación web, render_template para usar plantillas HTML, request para manejar datos de formularios, y redirect para redirigir páginas.
import mysql.connector  # Librería para conectarse a MySQL.

# Creamos la aplicación Flask
app = Flask(__name__)

# Función para obtener la conexión a la base de datos MySQL
def get_db_connection():
    return mysql.connector.connect( 
        host="localhost",   # Dirección del servidor de base de datos (local en este caso).
        user="root",        # Usuario de la base de datos.
        password="ACL2005", # Contraseña del usuario.
        database="agenda"   # Nombre de la base de datos que estamos usando.
    )

# Definimos una ruta en Flask para la página principal
@app.route("/")
def home():
    # Conectamos con la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Ejecutamos una consulta SQL para obtener todos los registros de la tabla "cumpleaños"
    cursor.execute("SELECT * FROM cumpleaños")

    # Obtenemos los resultados de la consulta y los almacenamos en una variable
    cumpleaños = cursor.fetchall()

    # Renderizamos la plantilla HTML "index.html" y pasamos los datos obtenidos como contexto
    return render_template("index.html", actividades=cumpleaños)
