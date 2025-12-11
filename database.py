#---------------------------------------------------------------------------------------------------------
#Importo el módulo sqlite3 y Path del módulo pathlib para establecer la conexión y poder rutear la base de datos

import sqlite3
from pathlib import Path
# ------------------------------------------------------------------------------------------------
# Función auxiliar para mostrar fecha/hora en consola para el historial
# ------------------------------------------------------------------------------------------------
from datetime import datetime

def ahora():
    """Devuelve fecha y hora actual con formato lindo para mostrar en consola"""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#---------------------------------------------------------------------------------------------------------
#Ruta donde guardo la base de datos
RUTA_BD = Path(__file__).with_name("inventario.db")

#---------------------------------------------------------------------------------------------------------

def conectar(): 
    return sqlite3.connect(RUTA_BD) 

#----------------------------------------------------------------------------------------------------------

def inicializar_bd():
    """Crea la tabla con los campos de fecha/hora que querías"""
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT,
            descripcion TEXT,
            stock INTEGER NOT NULL DEFAULT 0,
            fecha_registro TEXT NOT NULL DEFAULT (datetime('now')),
            ultima_modificacion TEXT,
            eliminado INTEGER NOT NULL DEFAULT 0,
            fecha_eliminacion TEXT
        )
    ''')
    
    conn.commit() #se guardan los cambios en la base de datos
    conn.close() #se cierra la base de datos para ahorrar recursos

#----------------------------------------------------------------------------------------------------------
# Funciones que utiliza la base de datos para las operaciones CRUD de mi sistema de gestión de inventario
#----------------------------------------------------------------------------------------------------------

def visualizar_listado_productos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, precio, categoria, descripcion, stock, 
               fecha_registro, ultima_modificacion 
        FROM productos 
        WHERE eliminado = 0
        ORDER BY nombre
    """)
    productos = cursor.fetchall()
    conn.close()
    return productos

#----------------------------------------------------------------------------------------------------------

def agregar_producto(nombre, precio, categoria="", descripcion="", stock=0):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO productos (nombre, precio, categoria, descripcion, stock)
    VALUES (:nombre, :precio, :categoria, :descripcion, :stock)
""", {"nombre": nombre, "precio": precio, "categoria": categoria, 
      "descripcion": descripcion, "stock": stock})
    conn.commit()
    conn.close()

#----------------------------------------------------------------------------------------------------------

def buscar_producto(termino):   
    conn = conectar()
    cursor = conn.cursor()
    termino = str(termino).strip().lower()   
    
    cursor.execute("""
        SELECT id, nombre, precio, categoria, descripcion, stock, fecha_registro, ultima_modificacion 
        FROM productos
        WHERE eliminado = 0
          AND (id = ? OR LOWER(nombre) LIKE ? OR LOWER(categoria) LIKE ?)
        ORDER BY nombre
    """, (termino, f"%{termino}%", f"%{termino}%"))
    
    resultado = cursor.fetchall()
    conn.close()
    return resultado


#----------------------------------------------------------------------------------------------------------

def eliminar_producto(id_eliminar):
    """Soft-delete + fecha de eliminación + última modificación"""  #Soft delete no se borra físicamente, se marca
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE productos 
        SET eliminado = 1,
            fecha_eliminacion = datetime('now'),
            ultima_modificacion = datetime('now')
        WHERE id = ? AND eliminado = 0
    """, (id_eliminar,))
    
    filas = cursor.rowcount
    conn.commit()
    conn.close()
    return filas > 0

#----------------------------------------------------------------------------------------------------------

def ver_papelera():
    """Visualiza los productos eliminados"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, precio, stock, fecha_eliminacion 
        FROM productos 
        WHERE eliminado = 1 
        ORDER BY fecha_eliminacion DESC
    """)
    papelera = cursor.fetchall()
    conn.close()
    return papelera

#----------------------------------------------------------------------------------------------------------

def restaurar_producto(id_prod):
    """Restaura un producto eliminado - vuelve al inventario"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE productos 
        SET eliminado = 0, 
            fecha_eliminacion = NULL,
            ultima_modificacion = datetime('now')
        WHERE id = ? AND eliminado = 1
    """, (id_prod,))
    filas = cursor.rowcount
    conn.commit()
    conn.close()
    return filas > 0

#----------------------------------------------------------------------------------------------------------

def borrar_definitivamente(id_prod):
    """Borra físicamente el producto de la base de datos"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ? AND eliminado = 1", (id_prod,))
    conn.commit()
    conn.close()



#----------------------------------------------------------------------------------------------------------


def actualizar_producto(id_prod, nombre=None, precio=None, categoria=None, descripcion=None, stock=None):
    """Actualiza solo los campos que el usuario cambió"""
    conn = conectar()
    cursor = conn.cursor()
    
    cambios_realizados = False
    
    if nombre is not None:
        cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nombre, id_prod))
        cambios_realizados = True
    
    if precio is not None:
        cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (precio, id_prod))
        cambios_realizados = True
    
    if categoria is not None:
        cursor.execute("UPDATE productos SET categoria = ? WHERE id = ?", (categoria, id_prod))
        cambios_realizados = True
    
    if descripcion is not None:
        cursor.execute("UPDATE productos SET descripcion = ? WHERE id = ?", (descripcion, id_prod))
        cambios_realizados = True
    
    if stock is not None:
        cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (stock, id_prod))
        cambios_realizados = True
    
    # Siempre actualizamos la fecha de última modificación
    cursor.execute("UPDATE productos SET ultima_modificacion = CURRENT_TIMESTAMP WHERE id = ?", (id_prod,))
    cambios_realizados = True
    
    if cambios_realizados:
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False  
#----------------------------------------------------------------------------------------------------------

def validar_stock(limite): 
    """reporta el estado del stock según una variable de cantidad especificada por el usuario"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, precio, categoria, descripcion, stock, fecha_registro 
        FROM productos 
        WHERE stock <= ? AND eliminado = 0
        ORDER BY stock
    """, (limite,))  
    bajo_stock = cursor.fetchall()
    conn.close()
    return bajo_stock

#---------------------------------------------------------------------------------------------------------

