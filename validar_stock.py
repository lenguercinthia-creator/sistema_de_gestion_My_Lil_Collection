# validar_stock.py - alerta de productos con poco stock

from database import validar_stock as obtener_bajos, visualizar_listado_productos as obtener_productos
from utils import esperar_enter
from database import ahora
from estilo import console, rprint, TITULO, EXITO, ADVERTENCIA

def ejecutar():
    console.rule(f"[{TITULO}] ALERTA DE STOCK BAJO - MY LIL COLLECTION")

    # Verifica si existen productos en la base de datos
    if not obtener_productos():
        rprint(f"[{ADVERTENCIA}]No hay productos cargados en el inventario aún")
        esperar_enter()
        return  

    while True:
        try:
            limite = int(input("\nHasta cuántas unidades considerás 'stock bajo'? (ej: 5): ").strip())
            if limite < 0:
                raise ValueError
            break
        except ValueError:
            rprint(f"[{ADVERTENCIA}]Por favor, ingresá un número válido y positivo.")
            
    productos_bajos = obtener_bajos(limite)
    
    if not productos_bajos:
        rprint(f"[{EXITO}]TODOS LOS PRODUCTOS TIENEN MÁS DE {limite} UNIDADES! -- {ahora()}")
        print("()")
    else:
        rprint(f"[{ADVERTENCIA}]ALERTA! HAY {len(productos_bajos)} PRODUCTO(S) CON STOCK BAJO O AGOTADO! -- {ahora()}")
        print("-" * 85)
        print(f"{'ID':<6} {'Nombre':<35} {'Stock':<10} {'Estado'}")
        print("-" * 85)
        for p in productos_bajos:
            # Desempaquetado  
            id_prod, nombre, precio, categoria, descripcion, stock, fecha_reg = p
            
            nombre = (nombre or "Sin nombre")[:34]
            stock = stock if stock is not None else 0
            estado = "AGOTADO" if stock == 0 else "BAJO"
            
            print(f"{id_prod:<6} {nombre:<35} {stock:<10} {estado}")
        print("-" * 85)
        rprint(f"[{ADVERTENCIA}]EMPEZÁ A TEJER!!!... {ahora()}")

    esperar_enter()
    
    
    
    