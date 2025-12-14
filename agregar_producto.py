# agregar_producto.py - agregar nuevos productos al inventario

from database import agregar_producto as agregar_en_bd
from database import visualizar_listado_productos as obtener_productos #para obtener el último ID
from utils import esperar_enter
from estilo import console, rprint, TITULO, EXITO, ADVERTENCIA, INFO
from rich.panel import Panel
from rich.table import Table
from database import ahora

def ejecutar():
    """Permite agregar un producto al inventario"""
    console.rule(f"[{TITULO}] AGREGANDO NUEVO PRODUCTO...")

    # Definimos las categorías disponibles
    categorias_disponibles = [
        "ropa", "accesorios", "hogar", "amigurumi", "deco", "bebé"
    ]

    # Mostrar opciones numeradas
    print("\nCategorías disponibles:")
    for i, cat in enumerate(categorias_disponibles, start=1):
        print(f"  {i}. {cat.capitalize()}")
    
    # Ingreso del nombre
    nombre = input("\nNombre del producto: ").strip()
    if not nombre:
        rprint(f"[{INFO}]El nombre no puede estar vacío.")
        esperar_enter()
        return

    # Ingreso del precio
    while True:
        precio_str = input("Precio del producto (ej: 450.50): ").strip()
        try:
            precio = float(precio_str.replace(",", "."))
            if precio < 0:
                raise ValueError
            break
        except ValueError:
            rprint(f"[{ADVERTENCIA}]Ingresá un número válido para el precio.")

    # Selección de categoría
    while True:
        cat_input = input("Elegí la categoría por número (ej: 1): ").strip()
        if cat_input.isdigit():
            cat_index = int(cat_input) - 1
            if 0 <= cat_index < len(categorias_disponibles):
                categoria = categorias_disponibles[cat_index]
                break
        rprint(f"[{ADVERTENCIA}]Ingresá un número válido para la categoría.")

    # Descripción opcional
    descripcion_input = input("Descripción (opcional): ").strip()
    descripcion = descripcion_input if descripcion_input else None

    # Stock
    while True:
        stock_str = input("Stock inicial (ej: 10): ").strip()
        if not stock_str:
            stock = 0
            break
        if stock_str.isdigit() and int(stock_str) >= 0:
            stock = int(stock_str)
            break
        rprint(f"[{ADVERTENCIA}]Ingresá un número válido para el stock.")

    # Guardamos en la base de datos
    agregar_en_bd(nombre, precio, categoria, descripcion, stock)

    # OBTENEMOS el ID del producto recién agregado
    productos = obtener_productos()
    ultimo_producto = productos[-1]  # el último es el que acabamos de agregar
    id_nuevo = ultimo_producto[0]

    # MOSTRAMOS el producto agregado 
    rprint(f"\n[{EXITO}]PRODUCTO AGREGADO CORRECTAMENTE! -- {ahora()}")

    table = Table(title=f"[bold plum1]Producto #{id_nuevo} agregado ♥[/bold plum1]", show_header=False, box=None)
    table.add_column(justify="right", style="cyan")
    table.add_column(justify="left", style="white")

    table.add_row("Nombre", nombre)
    table.add_row("Precio", f"${precio:,.2f}")
    table.add_row("Categoría", categoria.capitalize())
    table.add_row("Stock", str(stock))
    table.add_row("Descripción", descripcion or "Sin descripción")

    console.print(Panel(table, border_style="bright_magenta", padding=(1, 4)))

    rprint(f"[{EXITO}]♥ My Lil Collection está al día ♥")

    esperar_enter()
    
    