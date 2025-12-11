# utils.py
def esperar_enter():
    """Espera hasta que el usuario presione únicamente la tecla Enter"""
    while True:
        if input("\nPresioná Enter para continuar...").strip() == "":
            break
        
        