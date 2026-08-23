from crud import (
    registrar_empleado,
    mostrar_empleados,
    buscar_empleado,
    actualizar_empleado,
    eliminar_empleado
)

def menu_principal():
    while True:
        print("\n========================================")
        print("         CONTROL DE EMPLEADOS")
        print("========================================")
        print("             MENÚ GENERAL")
        print("----------------------------------------")
        print("1. Registrar empleado")
        print("2. Consultar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("6. Cerrar sesión")
        print("7. Salir")
        print("----------------------------------------")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            eliminar_empleado()
        elif opcion == "6":
            print("\nSesión finalizada correctamente.\n")
            break
        elif opcion == "7":
            print("\nPrograma cerrado.\n")
            exit()
        else:
            print("\nOpción incorrecta. Intente nuevamente.")