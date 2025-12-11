# menu.py - menú principal del sistema My Lil Collection
from estilo import console, rprint, TITULO, LINEA, ADVERTENCIA, ERROR #biblioteca Rich para estilos

list_opciones = [
    "Actualizar producto",
    "Agregar nuevo producto",
    "Buscar producto",
    "Eliminar producto",
    "Ver productos con poco stock",
    "Ver todo el catálogo",
    "Papelera de reciclaje",
    "Salir de My Lil Collection"
]

def menu(): 
    console.rule(f"[{TITULO}] MENÚ PRINCIPAL🧶")
    for i, texto in enumerate(list_opciones, start=1):
        print(f"   {i}. {texto}")
    console.rule(f"[{LINEA}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()


#-------------------------------------------------------------------------------

def opcion_input(): 
    """función para elegir opción del menú"""
    while True:
        try:
            opcion = int(input("Tu opción: "))
            if 1 <= opcion <= len(list_opciones):
                return opcion
            else:
                rprint(f"[{ERROR}]Opción inválida. Elegí un número del 1 al 8.")
        except ValueError:
            rprint(f"[{ADVERTENCIA}]Por favor, ingresá un número (no letras ni símbolos).")



