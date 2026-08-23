import sqlite3
import msvcrt

# Función para proteger la contraseña
def leer_password():
    password = ""
    while True:
        tecla = msvcrt.getwch()
        if tecla == "\r":
            print()
            break
        elif tecla == "\b":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += tecla
            print("*", end="", flush=True)

    return password


def iniciar_sesion():
    print("\n----------------------------------------")
    print("         CONTROL DE EMPLEADOS")
    print("----------------------------------------")
    print("            ACCESO AL SISTEMA")
    print("----------------------------------------")

    usuario = input("Usuario: ")
    print("Contraseña: ", end="", flush=True)
    password = leer_password()

    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE usuario = ? AND password = ?
    """, (usuario, password))

    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        print("\nAcceso correcto.")
        print("Bienvenido al sistema.\n")
        return True
    else:
        print("\nDatos de acceso incorrectos.")
        print("Intente nuevamente.\n")
        return False