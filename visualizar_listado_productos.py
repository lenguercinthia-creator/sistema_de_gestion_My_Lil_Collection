# visualizar_listado_productos.py - muestra todos los productos de la base de datos

from database import visualizar_listado_productos as obtener_productos
from utils import esperar_enter
from database import ahora
from estilo import console, rprint, TITULO, ADVERTENCIA, INFO


def ejecutar():
    console.rule(f"[{TITULO}] LISTADO COMPLETO DE PRODUCTOS - MY LIL COLLECTION")

    productos = obtener_productos()

    if not productos:
        rprint(f"[{ADVERTENCIA}]My Lil Collection está vacía - Hay que agregar stock... {ahora()}")
        rprint(f"[{INFO}]Volvé al menú y elegí la opción 2 para empezar a cargar productos.")
    else:
        rprint(f"[{INFO}]Total de productos registrados: {len(productos)}\n -- {ahora()}")

        # Cabecera con alineación a la izquierda
        print("-" * 95)
        print(f"{'ID':<4} {'Nombre':<25} {'Precio':<12} {'Categoría':<12} {'Descripción':<35} {'Stock':<6}")
        print("-" * 95)

        for p in productos:
            # Unpack flexible de las columnas
            id_prod, nombre, precio, categoria, descripcion, stock, *resto = p

            # Formateo de campos
            nombre = (nombre or "Sin nombre")[:25]
            precio_str = f"${precio:,.2f}" if precio is not None else "$0.00"
            categoria = (categoria or "Sin categoría")[:12]
            descripcion_corta = (descripcion or "N/A")
            if len(descripcion_corta) > 35:
                descripcion_corta = descripcion_corta[:32] + "..."
            stock = str(stock) if stock is not None else "0"

            # Impresión alineada a la izquierda
            print(f"{id_prod:<4} {nombre:<25} {precio_str:<12} {categoria:<12} {descripcion_corta:<35} {stock:<6}")

        print("-" * 95)

    esperar_enter()
    
    
    
    
