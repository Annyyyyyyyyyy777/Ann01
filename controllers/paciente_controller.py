from models.paciente import Paciente
from models.paciente_dao import PacienteDAO
from models.departamento_dao import DepartamentoDAO
from views.paciente_view import PacienteView

class PacienteController:
    def __init__(self):
        self.view = PacienteView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_paciente()
            elif opcion == 2:
                self.editar_paciente()
            elif opcion == 3:
                self.eliminar_paciente()
            elif opcion == 4:
                self.imprimir_paciente()
            elif opcion == 5:
                self.imprimir_pacientes()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestión de pacientes.")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")

    def agregar_paciente(self) -> None:
        departamentos = DepartamentoDAO.obtener_todos()
        datos = self.view.formulario_nuevo_paciente(departamentos)
        try:
            departamento_seleccionado = None
            if datos.get('id_departamento'):
                departamento_seleccionado = DepartamentoDAO.obtener_por_id(datos['id_departamento'])
                
            nuevo_paciente = Paciente(datos['rut'], datos['nombre'], datos['edad'], datos['prevision'], departamento_seleccionado)
            # Verificar si existe
            if PacienteDAO.obtener_por_rut(nuevo_paciente.rut):
                self.view.mostrar_mensaje(f"Error: Ya existe un paciente con RUT {nuevo_paciente.rut}")
                return
            
            exito = PacienteDAO.crear(nuevo_paciente)
            if exito:
                self.view.mostrar_mensaje("Paciente agregado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al guardar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos ingresados: {e}")

    def editar_paciente(self) -> None:
        rut = self.view.solicitar_rut()
        paciente = PacienteDAO.obtener_por_rut(rut)
        if not paciente:
            self.view.mostrar_mensaje("Paciente no encontrado.")
            return

        departamentos = DepartamentoDAO.obtener_todos()
        datos_nuevos = self.view.formulario_editar_paciente(paciente, departamentos)
        try:
            paciente.nombre = datos_nuevos['nombre']
            paciente.edad = datos_nuevos['edad']
            paciente.prevision = datos_nuevos['prevision']
            
            departamento_seleccionado = None
            if datos_nuevos.get('id_departamento'):
                departamento_seleccionado = DepartamentoDAO.obtener_por_id(datos_nuevos['id_departamento'])
            paciente.departamento = departamento_seleccionado
            
            exito = PacienteDAO.actualizar(paciente)
            if exito:
                self.view.mostrar_mensaje("Paciente actualizado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al actualizar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos modificados: {e}")

    def eliminar_paciente(self) -> None:
        rut = self.view.solicitar_rut()
        paciente = PacienteDAO.obtener_por_rut(rut)
        if not paciente:
            self.view.mostrar_mensaje("Paciente no encontrado.")
            return

        if self.view.confirmar_eliminacion(paciente.nombre):
            exito = PacienteDAO.eliminar(rut)
            if exito:
                self.view.mostrar_mensaje("Paciente eliminado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al eliminar en la base de datos.")
        else:
            self.view.mostrar_mensaje("Operación cancelada.")

    def imprimir_paciente(self) -> None:
        rut = self.view.solicitar_rut()
        paciente = PacienteDAO.obtener_por_rut(rut)
        if paciente:
            self.view.mostrar_paciente(paciente)
        else:
            self.view.mostrar_mensaje("Paciente no encontrado.")

    def imprimir_pacientes(self) -> None:
        pacientes = PacienteDAO.obtener_todos()
        self.view.mostrar_lista_pacientes(pacientes)