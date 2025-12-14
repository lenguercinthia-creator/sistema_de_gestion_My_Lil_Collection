# registrar_venta.py - registra las ventas realizadas

from database import (
    registrar_venta as venta,
    buscar_producto as buscar_en_bd,
    obtener_producto_por_id as obtener_id,
    ahora
)
from validar_stock import ejecutar as validar
from utils import esperar_enter
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from estilo import rprint, EXITO, ERROR, INFO, ADVERTENCIA

console = Console()


def ejecutar():
    """Permite registrar la venta de productos"""
    console.print(Panel(f"[bold green]REGISTRANDO VENTA...[/] - {ahora()}"))

    # Buscar producto
    termino = console.input("\n[bold yellow]Buscar producto por nombre o ID:[/] ")
    resultados = buscar_en_bd(termino)

    if not resultados:
        rprint(f"[{ERROR}]⚠ No se encontró ningún producto con '{termino}' ⚠")
        esperar_enter()
        return

    # Mostrar resultados
    tabla = Table(title="PRODUCTOS ENCONTRADOS")
    tabla.add_column("ID", style="cyan")
    tabla.add_column("Nombre", style="magenta")
    tabla.add_column("Categoría")
    tabla.add_column("Precio", justify="right")
    tabla.add_column("Stock", justify="right")

    for p in resultados:
        id_prod, nombre, precio, categoria, descripcion, stock, *_ = p
        stock_color = "red" if stock < 5 else "green"

        tabla.add_row(
            str(id_prod),
            nombre,
            categoria or "-",
            f"${precio:,.2f}",
            f"[{stock_color}]{stock}[/]"
        )

    console.print(tabla)

    # Elegir producto
    try:
        id_elegido = int(console.input("\n[bold]Ingrese el ID del producto a vender:[/] "))
    except ValueError:
        rprint(f"[{ERROR}]ID inválido")
        esperar_enter()
        return

    try:
        cantidad = int(console.input("[bold]Cantidad a vender:[/] "))
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        rprint(f"[{ERROR}]Cantidad inválida")
        esperar_enter()
        return

    # Obtener producto para resumen
    producto = obtener_id(id_elegido)

    if not producto:
        rprint(f"[{ADVERTENCIA}]Producto no encontrado o eliminado")
        esperar_enter()
        return

    id_elegido, nombre, precio, categoria, descripcion, stock, *_ = producto
    total_venta = precio * cantidad

    # Resumen
    console.print(Panel(
        f"[bold cyan]RESUMEN DE VENTA[/]\n\n"
        f"Producto: [bold]{nombre}[/bold]\n"
        f"Categoría: {categoria or '—'}\n"
        f"Descripción: {descripcion or 'Sin descripción'}\n"
        f"Cantidad: [bold]{cantidad}[/bold]\n"
        f"Precio unitario: [bold green]${precio:,.2f}[/]\n"
        f"Total a cobrar: [bold yellow]${total_venta:,.2f}[/]",
        style=INFO
    ))

    # Confirmación
    while True:
        confirmar = console.input("\n[bold green]¿Confirmar la venta? (s/n):[/] ").strip().lower()
        if confirmar in ("s", "si"):
            break
        if confirmar in ("n", "no"):
            rprint("[bold yellow]Venta cancelada[/bold yellow]")
            esperar_enter()
            return
        rprint(f"[{ERROR}]Respondé con 's' o 'n'")

    # Registrar venta
    exito, mensaje = venta(id_elegido, cantidad)

    if exito:
        rprint(Panel(mensaje, style=EXITO))
        validar()
    else:
        rprint(Panel(mensaje, style=ERROR))
        esperar_enter()
