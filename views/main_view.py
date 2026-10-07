from views.utils import leer_numero

class MainView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "="*30)
        print("    CLÍNICA - MENÚ PRINCIPAL")
        print("="*30)
        print("1.- Gestión de Pacientes")
        print("2.- Gestión de Departamentos")
        print("0.- Salir")
        print("="*30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[SISTEMA] {mensaje}")