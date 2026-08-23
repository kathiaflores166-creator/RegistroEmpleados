from login import iniciar_sesion
from menu import menu_principal 

while True:

    if iniciar_sesion():
        menu_principal()

    else:
        print("Intente nuevamente.\n")    