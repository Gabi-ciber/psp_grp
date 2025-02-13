def opcion1():
print("Opción 1 seleccionada")
def opcion2():
print("Opción 2 seleccionada")
def opcion3():
print("Opción 3 seleccionada")
def salir():
print("Saliendo del programa")
exit()
while True:
print("Menú:")
print("1. Opción 1")
print("2. Opción 2")
print("3. Opción 3")
print("4. Salir")
opcion = int(input("Seleccione una opción: "))
if opcion == 1:
opcion1()
elif opcion == 2:
opcion2()
elif opcion == 3:
opcion3()
elif opcion == 4:
salir()
else:
print("Opción inválida. Por favor, seleccione una opción válida.")
import psycopg2
from conexion import conectar_bd, cerrar_conexion
def opcion1():
conn = conectar_bd()
if conn:
print("Opción 1 seleccionada - Conectado a la base de datos")
cerrar_conexion(conn)
def opcion2():
conn = conectar_bd()
if conn:
print("Opción 2 seleccionada - Conectado a la base de datos")
cerrar_conexion(conn)
def opcion3():
conn = conectar_bd()
if conn:
print("Opción 3 seleccionada - Conectado a la base de datos")
cerrar_conexion(conn)
def salir():
print("Saliendo del programa")
exit()
while True:
print("Menú:")
print("1. Opción 1")
print("2. Opción 2")
print("3. Opción 3")
print("4. Salir")
opcion = int(input("Seleccione una opción: "))
if opcion == 1:
opcion1()
elif opcion == 2:
opcion2()
elif opcion == 3:
opcion3()
elif opcion == 4:
salir()
else:
print("Opción inválida. Por favor, seleccione una opción válida.")
