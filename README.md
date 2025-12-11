# Sistema de Gestión My Lil Collection🧶

**Versión 1.0** – En español.
Sistema de gestión de inventario en consola.

Este proyecto es mi primer incursión a Python y mi primera versión completa de un catálogo para organizar creaciones de un pequeño emprendimiento.  
Cuenta con control total de productos, stock, precios y fechas, y una interfaz a color en consola.

## - Estado actual: Versión 1.0 (Consola)

- Funcionalidades completas de CRUD (Crear, Leer, Actualizar, Eliminar)
- Alertas de stock bajo
- Colores y tablas con Rich
- Base de datos SQLite con datos de prueba incluidos
- Registro automático de fechas y timestamps

## - Tecnologías usadas

- Python 3
- SQLite (base de datos local)
- Rich (para colores y tablas en consola)

## - Estructura del proyecto

My-Lil-Collection/
├── main.py                      # Menú principal

├── database.py                  # Conexión y operaciones con SQLite

├── agregar_producto.py          # Funcionalidades separadas

├── buscar_producto.py

├── visualizar_listado_productos.py

├── editar_producto.py

├── eliminar_producto.py

└── validar_stock.py

├── inventario.db                # Base de datos con datos de prueba incluidos

├── requirements.txt

├── .gitignore

└── README.md


## - Roadmap – Próximas versiones

Planeo seguir desarrollándolo con estas mejoras:

- [ ] Interfaz gráfica (GUI) con Tkinter o CustomTkinter
- [ ] Fotos de cada producto
- [ ] Categorías y filtros avanzados
- [ ] Reportes de ventas y ganancias
- [ ] Exportar a PDF o Excel
- [ ] Modo oscuro y temas personalizados
- [ ] Posible versión web con Flask o Streamlit

Seguime en el repositorio para ver las actualizaciones!

## - Ejecución inmediata

- El repositorio incluye una base de datos con productos de ejemplo.  
- Al clonar y ejecutar `python main.py`, vas a ver productos de prueba en el listado.

## - Instalación y uso

1. Cloná el repositorio

   ```powershell
   git clone https://github.com/lenguercinthia-creator/My-Lil-Collection.git
   cd My-Lil-Collection

2. Instalá las dependencias:

   pip install -r requirements.txt

3. Ejecutá la aplicación:
   
   python main.py

## - Tips

- Presioná solo Enter en los menús para continuar
- El stock bajo se alerta según el umbral que definas en el código

## 💜- Licencia
  - MIT License - Sentite libre de usar, modificar y compartir
  -  Gracias por visitar mi proyecto!

