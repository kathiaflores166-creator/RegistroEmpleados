import sqlite3

# Crear conexión
conexion = sqlite3.connect("empleados.db")

# Crear cursor
cursor = conexion.cursor()

# Tabla usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Tabla empleados
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL,
    telefono TEXT,
    correo TEXT
)
""")

# Verificar si existe el administrador
cursor.execute("SELECT * FROM usuarios WHERE usuario='admin'")
usuario = cursor.fetchone()

# Crear administrador si no existe
if usuario is None:
    cursor.execute("""
        INSERT INTO usuarios(usuario, password)
        VALUES(?, ?)
    """, ("admin", "1234"))

# Guardar cambios
conexion.commit()

# Cerrar conexión
conexion.close()

print("Base de datos creada correctamente.")
