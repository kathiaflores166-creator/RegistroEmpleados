import sqlite3

def registrar_empleado():

    print("\n===== REGISTRAR EMPLEADO =====\n")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo: ")
    salario = float(input("Salario: "))
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
INSERT INTO empleados(
    nombre,
    apellido,
    cargo,
    salario,
    telefono,
    correo
)
VALUES(?,?,?,?,?,?)
""", (nombre, apellido, cargo, salario, telefono, correo))

    conexion.commit()

    conexion.close()

    print("\nEmpleado registrado correctamente.\n")

def mostrar_empleados():

    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM empleados
    """)

    empleados = cursor.fetchall()

    conexion.close()

    print("\n===== LISTA DE EMPLEADOS =====\n")

    if len(empleados) == 0:
        print("No existen empleados registrados.")
        return

    print(f"{'ID':<5}{'Nombre':<15}{'Apellido':<15}{'Cargo':<20}{'Salario':<12}")
    print("-"*67)

    for empleado in empleados:
        print(f"{empleado[0]:<5}"
              f"{empleado[1]:<15}"
              f"{empleado[2]:<15}"
              f"{empleado[3]:<20}"
              f"${float(str(empleado[4]).replace('$', '')):<10.2f}")

def buscar_empleado():

    print("\n===== BUSCAR EMPLEADO =====\n")

    id_empleado = input("Ingrese el ID del empleado: ")

    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM empleados
    WHERE id = ?
    """, (id_empleado,))

    empleado = cursor.fetchone()

    conexion.close()

    if empleado:

        print("\n==============================")

        print(f"ID:       {empleado[0]}")
        print(f"Nombre:   {empleado[1]}")
        print(f"Apellido: {empleado[2]}")
        print(f"Cargo:    {empleado[3]}")
        print(f"Salario:  ${empleado[4]:.2f}")
        print(f"Teléfono: {empleado[5]}")
        print(f"Correo:   {empleado[6]}")

        print("==============================\n")

    else:

        print("\nEmpleado no encontrado.\n")

import sqlite3


def actualizar_empleado():

    print("\n===== ACTUALIZAR EMPLEADO =====\n")

    id_empleado = input("Ingrese el ID del empleado a actualizar: ")

    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    # Verificar si existe el empleado
    cursor.execute("""
    SELECT * FROM empleados
    WHERE id = ?
    """, (id_empleado,))

    empleado = cursor.fetchone()

    if empleado is None:
        print("\nEmpleado no encontrado.\n")
        conexion.close()
        return

    print("\nDatos actuales del empleado:")
    print(f"Nombre    : {empleado[1]}")
    print(f"Apellido  : {empleado[2]}")
    print(f"Cargo     : {empleado[3]}")
    print(f"Salario   : ${float(str(empleado[4]).replace('$', '')):.2f}")
    print(f"Teléfono  : {empleado[5]}")
    print(f"Correo    : {empleado[6]}")

    print("\nIngrese los nuevos datos:")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo: ")

    while True:
        try:
            salario = float(input("Salario: "))
            break
        except ValueError:
            print("Ingrese un salario válido.")

    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    cursor.execute("""
    UPDATE empleados
    SET
        nombre = ?,
        apellido = ?,
        cargo = ?,
        salario = ?,
        telefono = ?,
        correo = ?
    WHERE id = ?
    """, (
        nombre,
        apellido,
        cargo,
        salario,
        telefono,
        correo,
        id_empleado
    ))

    conexion.commit()
    conexion.close()

    print("\nEmpleado actualizado correctamente.\n")

def eliminar_empleado():

    print("\n===== ELIMINAR EMPLEADO =====\n")

    id_empleado = input("Ingrese el ID del empleado: ")

    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    # Buscar el empleado
    cursor.execute("""
        SELECT *
        FROM empleados
        WHERE id = ?
    """, (id_empleado,))

    empleado = cursor.fetchone()

    if empleado is None:
        print("\nEmpleado no encontrado.\n")
        conexion.close()
        return

    print("\nEmpleado encontrado:\n")

    print(f"ID: {empleado[0]}")
    print(f"Nombre: {empleado[1]}")
    print(f"Apellido: {empleado[2]}")
    print(f"Cargo: {empleado[3]}")
    print(f"Salario: ${empleado[4]:.2f}")

    respuesta = input("\n¿Está seguro que desea eliminar este empleado? (S/N): ")

    if respuesta.upper() == "S":

        cursor.execute("""
            DELETE FROM empleados
            WHERE id = ?
        """, (id_empleado,))

        conexion.commit()

        print("\nEmpleado eliminado correctamente.\n")

    else:

        print("\nOperación cancelada.\n")

    conexion.close()