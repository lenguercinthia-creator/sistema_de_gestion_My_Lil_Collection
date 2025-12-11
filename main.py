# main.py contiene el flujo principal del sistema de gestión
# importo las funciones necesarias de otros módulos
from database import inicializar_bd
from menu import menu, opcion_input  
from actualizar_producto import ejecutar as actualizar
from agregar_producto import ejecutar as agregar
from buscar_producto import ejecutar as buscar
from eliminar_producto import ejecutar as eliminar
from validar_stock import ejecutar as validar 
from visualizar_listado_productos import ejecutar as visualizar
import papelera
from salir import ejecutar as salir  
from estilo import console, rprint, TITULO, ERROR
from datetime import datetime
import locale

# Forzamos español para que muestre la fecha y hora
try:
    locale.setlocale(locale.LC_TIME, 'es_AR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Spanish_Argentina.1252')
    except:
        locale.setlocale(locale.LC_TIME, '')

#------------------------------------------------------------------------------------------------------

inicializar_bd()  # ← solo una vez al inicio


# === BIENVENIDA (solo se muestra al entrar al menú) ===
console.rule(f"[{TITULO}] SISTEMA DE GESTIÓN DE MY LIL COLLECTION")
rprint("[bold plum1]               ♥ Tu tienda de crochet ♥[/bold plum1]")

ahora = datetime.now()
fecha_hora = ahora.strftime("%A %d de %B de %Y - %H:%M:%S").replace(" 0", " ")
rprint(f"\n[bold medium_purple]{fecha_hora.upper()}[/bold medium_purple]\n")

console.rule(f"[{TITULO}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


while True:
    console.print()
    rprint("[bold cyan]Elegí una opción del menú:[/bold cyan]\n")
    
    menu()
    """muestra el menú principal y obtiene la opción del usuario"""                     
    opcion = opcion_input()

    match opcion:
        case 1: 
            actualizar()
        case 2: 
            agregar()
        case 3: 
            buscar()
        case 4: 
            eliminar()
        case 5: 
            validar()
        case 6: 
            visualizar()
        case 7: 
            papelera.menu_papelera()
        case 8:
            salir()           
            break             
        case _: 
            rprint(f"[{ERROR}]Opción no válida, intentá denuevo.\n")
            
            
            
            
            