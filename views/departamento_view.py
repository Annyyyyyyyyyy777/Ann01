from views.utils import leer_numero, confirmar
from models.departamento import Departamento

class DepartamentoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-"*30)
        print(" GESTIÓN DE DEPARTAMENTOS")
        print("-"*30)
        print("1.- Agregar departamento")
        print("2.- Editar departamento")
        print("3.- Eliminar departamento")
        print("4.- Imprimir un departamento")
        print("5.- Imprimir todos los departamentos")
        print("0.- Volver al menú principal")
        print("-"*30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_departamento() -> dict:
        print("\n--- Agregar Nuevo Departamento ---")
        nombre = input("Ingrese el nombre del departamento: ")
        piso = leer_numero("Ingrese el piso (número): ")
        
        return {
            "nombre": nombre,
            "piso": piso
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese el ID del departamento: ")

    @staticmethod
    def mostrar_departamento(departamento: Departamento) -> None:
        print("\n--- Datos del Departamento ---")
        print(departamento)
        print("-" * 30)

    @staticmethod
    def mostrar_lista_departamentos(departamentos: list[Departamento]) -> None:
        print("\n--- Lista de Departamentos ---")
        if not departamentos:
            print("No hay departamentos registrados.")
        else:
            for d in departamentos:
                print(d)
        print("-" * 30)

    @staticmethod
    def formulario_editar_departamento(departamento: Departamento) -> dict:
        print(f"\n--- Editando Departamento [ID: {departamento.id_departamento}] ---")
        print("Deje en blanco si no desea modificar el campo de texto.")
        
        nuevo_nombre = input(f"Nombre actual ({departamento.nombre}): ")
        if not nuevo_nombre.strip():
            nuevo_nombre = departamento.nombre
            
        nuevo_piso_input = input(f"Piso actual ({departamento.piso}): ")
        try:
            nuevo_piso = int(nuevo_piso_input) if nuevo_piso_input.strip() else departamento.piso
        except ValueError:
            nuevo_piso = departamento.piso

        return {
            "id_departamento": departamento.id_departamento,
            "nombre": nuevo_nombre,
            "piso": nuevo_piso
        }

    @staticmethod
    def confirmar_eliminacion(nombre: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar el departamento '{nombre}'?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[DEPARTAMENTOS] {mensaje}")