import psycopg2 #añado comentario extra 
def conectar_bd():
try:
conexion = psycopg2.connect(
dbname="pruebaPPS",
user="tu_usuario",
password="tu_contraseña gabi",
host="localhost", # Cambia si el servidor no está en local
port="5435" # Puerto por defecto de PostgreSQL cambio puerto
)
print("Conexión exitosa a la base de datos")
return conexion
except Exception as e:
print(f"Error al conectar a la base de datos: {e}")
return None
def cerrar_conexion(conexion):
if conexion:
conexion.close()
print("Conexión cerrada")
if __name__ == "__main__":
conn = conectar_bd()
cerrar_conexion(conn)
