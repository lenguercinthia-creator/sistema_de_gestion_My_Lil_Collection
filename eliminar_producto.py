# eliminar_producto.py
from database import eliminar_producto as eliminar_en_bd
from database import visualizar_listado_productos as obtener_productos
from utils import esperar_enter
from database import ahora
from estilo import console, rprint, TITULO, EXITO, INFO, ERROR

def ejecutar():
    console.rule(f"[{TITULO}] ELIMINANDO PRODUCTO...")

    productos = obtener_productos()
    if not productos:
        rprint(f"[{INFO}]No hay productos registrados para eliminar.")
        esperar_enter()
        return

    # Mostrar listado
    print("\nProductos disponibles:")
    print(f"{'ID':<4} {'Nombre':<25} {'Precio':<12} {'Categoría':<12} {'Descripción':<35} {'Stock':<6}")
    print("-" * 95)

    for p in productos:
        # Unpack flexible
        id_prod, nombre, precio, categoria, descripcion, stock, *resto = p

        # Formateo
        nombre = (nombre or "Sin nombre")[:25]
        precio_str = f"${precio:,.2f}" if precio is not None else "$0.00"
        categoria = (categoria or "N/A")[:12]
        descripcion_corta = (descripcion or "N/A")
        if len(descripcion_corta) > 35:
            descripcion_corta = descripcion_corta[:32] + "..."
        stock = str(stock) if stock is not None else "0"

        print(f"{id_prod:<4} {nombre:<25} {precio_str:<12} {categoria:<12} {descripcion_corta:<35} {stock:<6}")

    print("-" * 95)

    # Pedir ID a eliminar
    while True:
        entrada = input("\nIngresá el ID del producto a eliminar (o 'S' para cancelar): ").strip()
        if entrada.upper() == "S":
            rprint(f"[{INFO}]Operación cancelada.")
            esperar_enter()
            return
        if entrada.isdigit():
            id_eliminar = int(entrada)
            break
        rprint(f"[{ERROR}]El ID debe ser un número.")

    # Verificar si existe
    producto = next((p for p in productos if p[0] == id_eliminar), None)
    if not producto:
        rprint(f"[{ERROR}]No existe ningún producto con ID {id_eliminar}")
        esperar_enter()
        return

    nombre = producto[1]
    print(f"\nProducto encontrado: {nombre} (ID {id_eliminar})")

    # Confirmación
    while True:
        confirm = input(f"⚠Seguro que querés eliminar '{nombre}'? (S/N): ").strip().upper()
        if confirm == "S":
            eliminar_en_bd(id_eliminar)
            rprint(f"[{EXITO}]PRODUCTO ELIMINADO CORRECTAMENTE. -- {ahora()}")
            break
        elif confirm == "N":
            rprint(f"[{INFO}]Eliminación cancelada.")
            break
        else:
            rprint(f"[{ERROR}]Por favor, respondé con S (sí) o N (no).")

    esperar_enter()
    
    
