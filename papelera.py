# papelera.py - para ver y gestionar la papelera de reciclaje
import database as db
from utils import esperar_enter
from database import ahora
from estilo import console, rprint

# ---------------------------------------------------------------------------
def mostrar_papelera():
    """Muestra los productos eliminados (papelera)"""
    productos = db.ver_papelera()

    console.rule("[bold magenta]PAPELERA DE RECICLAJE[/bold magenta]")

    if not productos:
        rprint("\n[grey58]La papelera está vacía!")
        esperar_enter()
        return True

    # Cabecera alineada a la izquierda
    print(f"{'ID':<6} {'Nombre':<36} {'Precio':<12} {'Stock':<8} {'Eliminado el'}")
    console.rule("[grey58]" + "─" * 88)

    for p in productos:
        # desempaquetamos solo las 5 columnas que sabemos que existen
        id_prod, nombre, precio, stock, fecha_eli = p

        # Formateo seguro
        nombre = (nombre or "Sin nombre")[:36]
        precio = precio if precio is not None else 0.0
        stock = stock if stock is not None else 0
        fecha = fecha_eli or "─"

        print(f"{id_prod:<6} {nombre:<36} ${precio:<10,.2f} {stock:<8} {fecha}")

    return False

# ---------------------------------------------------------------------------
def restaurar_producto():
    """Restaura un producto eliminado"""
    try:
        id_rest = int(input("\nID del producto a restaurar: "))
        if db.restaurar_producto(id_rest):
            rprint(f"\n[bold green]Producto {id_rest} restaurado correctamente -- {ahora()}")
        else:
            rprint(f"\n[bold red]No se encontró el ID {id_rest} en la papelera")
    except ValueError:
        rprint("[red]Ingresá un número válido[/red]")
    esperar_enter()
    

# ---------------------------------------------------------------------------
def borrar_definitivamente():
    """Borra físicamente un producto eliminado"""
    try:
        id_borrar = int(input("\nID del producto a borrar PARA SIEMPRE: "))
        confirm = input(f"\n¿Eliminar definitivamente el ID {id_borrar}? (s/N): ")
        if confirm.lower() == "s":
            db.borrar_definitivamente(id_borrar)
            rprint(f"\n[bold red]Producto {id_borrar} eliminado para siempre... -- {ahora()}")
        else:
            rprint("\n[grey58]Operación cancelada")
    except ValueError:
        rprint("[red]ID inválido[/red]")
    esperar_enter()
    

# ---------------------------------------------------------------------------
def menu_papelera():
    """Menú de opciones de la papelera"""
    while True:
        vacia = mostrar_papelera()
        if vacia:
            return

        print("\nOpciones:")
        print("1. Restaurar producto")
        print("2. Borrar permanentemente")
        print("0. Volver al menú principal")
        console.rule("[grey58]" + "─" * 40)

        opcion = input("\nElige: ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            restaurar_producto()
        elif opcion == "2":
            borrar_definitivamente()
        else:
            rprint("[red]Opción inválida[/red]")
            esperar_enter()
        
            