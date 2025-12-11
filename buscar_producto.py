# buscar_producto.py
from database import buscar_producto as buscar_en_bd, visualizar_listado_productos as obtener_productos
from utils import esperar_enter
from database import ahora
from estilo import console, rprint, TITULO, INFO, ERROR, ADVERTENCIA

def ejecutar():
    """Función para buscar un producto por ID, nombre o categoría"""
    console.rule(f"[{TITULO}] BUSCANDO PRODUCTO...")

    # Verificamos si hay algo en la base de datos
    todos_los_productos = obtener_productos()
    if not todos_los_productos:
        rprint(f"[{ADVERTENCIA}]Aún no hay productos en My Lil Collection -- {ahora()}")
        rprint(f"[{INFO}]Volvé al menú principal y elegí la opción 2 para empezar a cargar stock.")
        esperar_enter()
        return

    # Entrada de búsqueda
    termino = input("\nIngresá ID, nombre o categoría a buscar o 'S' para volver: ").strip()
    if termino.upper() == "S":
        return

    if not termino:
        rprint(f"[{ERROR}]No ingresaste nada. Volvé a intentarlo.")
        esperar_enter()
        return

    resultados = buscar_en_bd(termino)

    if not resultados:
        rprint(f"[{INFO}]No se encontró ningún producto con '[bold]{termino}[/bold]'")
    else:
        rprint(f"[{INFO}]Se encontraron {len(resultados)} producto(s):\n -- {ahora()}")

        print("-" * 95)
        print(f"{'ID':<4} {'Nombre':<25} {'Precio':<12} {'Categoría':<12} {'Descripción':<35} {'Stock':<6}")
        print("-" * 95)

        for p in resultados:
            # Unpack flexible para columnas extra
            id_prod, nombre, precio, categoria, descripcion, stock, *resto = p

            # Formateo
            nombre = (nombre or "Sin nombre")[:25]
            precio_str = f"${precio:,.2f}" if precio is not None else "$0.00"
            categoria = (categoria or "Sin categoría")[:12]
            descripcion_corta = (descripcion or "N/A")
            if len(descripcion_corta) > 35:
                descripcion_corta = descripcion_corta[:32] + "..."
            stock = str(stock) if stock is not None else "0"

            print(f"{id_prod:<4} {nombre:<25} {precio_str:<12} {categoria:<12} {descripcion_corta:<35} {stock:<6}")

        print("-" * 95)

    esperar_enter()
    
    
