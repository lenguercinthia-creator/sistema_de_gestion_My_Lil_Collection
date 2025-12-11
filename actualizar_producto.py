# actualizar_producto.py - Modificar productos existentes 
from database import actualizar_producto as actualizar_en_bd
from database import visualizar_listado_productos as obtener_productos
from utils import esperar_enter
from database import ahora
from estilo import console, rprint, TITULO, EXITO, ERROR, INFO, ADVERTENCIA


def ejecutar():
    """Permite editar un producto existente"""
    print("\n" + "═" * 50)
    console.rule(f"[{TITULO}]ACTUALIZANDO PRODUCTO...")
    print("═" * 50)

    productos = obtener_productos()
    if not productos:
        rprint(f"[{INFO}]Todavía no hay productos en el inventario.")
        esperar_enter()
        return

    # Listado rápido
    print("\nProductos actuales:")
    for p in productos:
        print(f"  ID {p[0]:<4} → {p[1]:<30} (Stock: {p[5]})")

    # Seleccionar ID
    while True:
        entrada = input("\nIngresá el ID del producto a editar (o 'S' para salir): ").strip()
        if entrada.upper() == "S":
            return
        if not entrada.isdigit():
            rprint(f"[{ERROR}]El ID debe ser un número.")
            continue
        id_prod = int(entrada)
        break

    # Verificar que exista
    producto = next((p for p in productos if p[0] == id_prod), None)
    if not producto:
        rprint(f"[{ERROR}]No existe un producto con ID {id_prod}")
        esperar_enter()
        return

    # Datos actuales
    id_prod, nombre_act, precio_act, cat_act, desc_act, stock_act, fecha_reg, ultima_mod = producto

    rprint(f"\n[{INFO}]Editando → [bold]{nombre_act}[/]")
    rprint(f"[{ADVERTENCIA}]Dejá en blanco para mantener el valor actual\n")

    # Pedir nuevos valores
    nuevo_nombre = input(f"   Nombre     [{nombre_act}]: ").strip()
    nuevo_nombre = nuevo_nombre if nuevo_nombre else nombre_act

    precio_input = input(f"   Precio     [${precio_act:,.2f}]: ").strip()
    nuevo_precio = float(precio_input.replace(",", ".")) if precio_input else precio_act

    nueva_cat = input(f"   Categoría  [{cat_act or 'Sin categoría'}]: ").strip()
    nueva_cat = nueva_cat if nueva_cat else cat_act

    nueva_desc = input(f"   Descripción[{desc_act or 'Sin descripción'}]: ").strip()
    nueva_desc = nueva_desc if nueva_desc else desc_act

    stock_input = input(f"   Stock      [{stock_act}]: ").strip()
    nuevo_stock = int(stock_input) if stock_input else stock_act

    # Confirmación antes de guardar
    print("\n" + "─" * 60)
    print("   NUEVOS VALORES:")
    print(f"   Nombre      → {nuevo_nombre}")
    print(f"   Precio      → ${nuevo_precio:,.2f}")
    print(f"   Categoría   → {nueva_cat or 'Sin categoría'}")
    print(f"   Descripción → {nueva_desc or 'Sin descripción'}")
    print(f"   Stock       → {nuevo_stock}")
    print("─" * 60)

    if input("\n¿Guardar cambios? (S/N): ").strip().upper() != "S":
        rprint(f"\n[{ADVERTENCIA}]Cambios cancelados.")
        esperar_enter()
        return

    # pasamos None solo cuando el usuario ESCRIBIÓ algo
    actualizar_en_bd(
        id_prod,
        nombre=nuevo_nombre if nuevo_nombre != nombre_act else None,
        precio=nuevo_precio if precio_input else None,           
        categoria=nueva_cat if nueva_cat != cat_act else None,
        descripcion=nueva_desc if nueva_desc != desc_act else None,
        stock=nuevo_stock if stock_input else None               
    )

    rprint(f"\n[{EXITO}]PRODUCTO ACTUALIZADO CORRECTAMENTE! -- {ahora()}")
    rprint(f"[{EXITO}]♥ My Lil Collection está al día ♥")

    esperar_enter()
    
    