from views.utils import leer_numero, confirmar
from models.paciente import Paciente
from models.departamento import Departamento

class PacienteView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-"*30)
        print("   GESTIÓN DE PACIENTES")
        print("-"*30)
        print("1.- Agregar paciente")
        print("2.- Editar paciente")
        print("3.- Eliminar paciente")
        print("4.- Imprimir un paciente")
        print("5.- Imprimir todos los pacientes")
        print("0.- Volver al menú principal")
        print("-"*30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def formulario_nuevo_paciente(departamentos: list[Departamento]) -> dict:
        print("\n--- Agregar Nuevo Paciente ---")
        rut = input("Ingrese el RUT del paciente (ej: 12.345.678-9): ")
        nombre = input("Ingrese el nombre del paciente: ")
        edad = leer_numero("Ingrese edad del paciente: ")
        print("Previsiones disponibles: 1.- Fonasa, 2.- Isapre, 3.- Particular, 4.- Otro")
        opcion_prev = leer_numero("Seleccione una previsión (1-4): ")
        mapa_prev = {1: "Fonasa", 2: "Isapre", 3: "Particular", 4: "Otro"}
        prevision = mapa_prev.get(opcion_prev, "")
        
        print("\nDepartamentos disponibles:")
        if departamentos:
            for d in departamentos:
                print(f"{d.id_departamento}.- {d.nombre} (Piso {d.piso})")
        else:
            print("No hay departamentos registrados.")
        
        opcion_depto = leer_numero("Seleccione el ID del departamento (o 0 para ninguno): ")
        id_departamento = opcion_depto if opcion_depto > 0 else None
        
        return {
            "rut": rut,
            "nombre": nombre,
            "edad": edad,
            "prevision": prevision,
            "id_departamento": id_departamento
        }

    @staticmethod
    def solicitar_rut() -> str:
        return input("Ingrese el RUT del paciente: ").strip()

    @staticmethod
    def mostrar_paciente(paciente: Paciente) -> None:
        print("\n--- Datos del Paciente ---")
        print(paciente)
        print("-" * 26)

    @staticmethod
    def mostrar_lista_pacientes(pacientes: list[Paciente]) -> None:
        print("\n--- Lista de Pacientes ---")
        if not pacientes:
            print("No hay pacientes registrados.")
        else:
            for p in pacientes:
                print(p)
        print("-" * 26)

    @staticmethod
    def formulario_editar_paciente(paciente: Paciente, departamentos: list[Departamento]) -> dict:
        print(f"\n--- Editando Paciente {paciente.nombre} ---")
        print("Deje en blanco si no desea modificar el campo de texto. Ingrese -1 para edad.")
        
        nuevo_nombre = input(f"Nombre actual ({paciente.nombre}): ")
        if not nuevo_nombre.strip():
            nuevo_nombre = paciente.nombre
            
        nueva_edad_input = input(f"Edad actual ({paciente.edad}): ")
        try:
            nueva_edad = int(nueva_edad_input) if nueva_edad_input.strip() else paciente.edad
        except ValueError:
            nueva_edad = paciente.edad
            
        print(f"Previsión actual ({paciente.prevision})")
        print("Previsiones disponibles: 1.- Fonasa, 2.- Isapre, 3.- Particular, 4.- Otro (0 para mantener actual)")
        opcion_prev = leer_numero("Seleccione una previsión: ")
        mapa_prev = {1: "Fonasa", 2: "Isapre", 3: "Particular", 4: "Otro"}
        nueva_prevision = mapa_prev.get(opcion_prev, paciente.prevision)

        print("\nDepartamentos disponibles:")
        if departamentos:
            for d in departamentos:
                print(f"{d.id_departamento}.- {d.nombre} (Piso {d.piso})")
        else:
            print("No hay departamentos registrados.")
            
        depto_actual_str = paciente.departamento.id_departamento if paciente.departamento else "Ninguno"
        opcion_depto_input = input(f"Seleccione nuevo ID de departamento (Actual: {depto_actual_str}, deje en blanco para mantener, 0 para quitar): ")
        
        depto_id = paciente.departamento.id_departamento if paciente.departamento else None
        
        if not opcion_depto_input.strip():
            nuevo_id_departamento = depto_id
        else:
            try:
                op_d = int(opcion_depto_input)
                nuevo_id_departamento = op_d if op_d > 0 else None
            except ValueError:
                nuevo_id_departamento = depto_id

        return {
            "rut": paciente.rut, # El RUT no se edita normalmente (es PK)
            "nombre": nuevo_nombre,
            "edad": nueva_edad,
            "prevision": nueva_prevision,
            "id_departamento": nuevo_id_departamento
        }

    @staticmethod
    def confirmar_eliminacion(nombre: str) -> bool:
        return confirmar(f"¿Está seguro que desea eliminar al paciente {nombre}?")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[PACIENTES] {mensaje}")