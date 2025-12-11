# salir.py
from utils import esperar_enter
from estilo import console, rprint, TITULO

def ejecutar():
    """Sale de la app"""
    console.rule(f"[{TITULO}] 💜Gracias por usar My Lil Collection!🧶")
    rprint("[bold plum1]⏳Saliendo del sistema...")
    esperar_enter()
    
    