from sqlite3 import Cursor
from config.database import Database
from models.paciente import Paciente
from models.departamento_dao import DepartamentoDAO

class PacienteDAO:
    """
    Data Access Object para la entidad Paciente.
    Maneja todas las operaciones CRUD en la base de datos.
    """

    @staticmethod
    def crear(paciente: Paciente) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            id_depto = paciente.departamento.id_departamento if paciente.departamento else None
            cursor.execute(
                "INSERT INTO paciente (rut, nombre, edad, prevision, id_departamento) VALUES (?, ?, ?, ?, ?)",
                (paciente.rut, paciente.nombre, paciente.edad, paciente.prevision, id_depto)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear paciente en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[Paciente]:
        conn = Database().get_connection()
        pacientes = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT rut, nombre, edad, prevision, id_departamento FROM paciente")
            filas = cursor.fetchall()
            for fila in filas:
                departamento = None
                if fila['id_departamento'] is not None:
                    departamento = DepartamentoDAO.obtener_por_id(fila['id_departamento'])
                pacientes.append(Paciente(fila['rut'], fila['nombre'], fila['edad'], fila['prevision'], departamento))
        except Exception as e:
            print(f"Error al obtener pacientes: {e}")
        finally:
            conn.close()
        return pacientes

    @staticmethod
    def obtener_por_rut(rut: str) -> Paciente | None:
        conn = Database().get_connection()
        paciente = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT rut, nombre, edad, prevision, id_departamento FROM paciente WHERE rut = ?", (rut.upper(),))
            fila = cursor.fetchone()
            if fila:
                departamento = None
                if fila['id_departamento'] is not None:
                    departamento = DepartamentoDAO.obtener_por_id(fila['id_departamento'])
                paciente = Paciente(fila['rut'], fila['nombre'], fila['edad'], fila['prevision'], departamento)
        except Exception as e:
            print(f"Error al obtener el paciente: {e}")
        finally:
            conn.close()
        return paciente

    @staticmethod
    def actualizar(paciente: Paciente) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            id_depto = paciente.departamento.id_departamento if paciente.departamento else None
            cursor.execute(
                "UPDATE paciente SET nombre = ?, edad = ?, prevision = ?, id_departamento = ? WHERE rut = ?",
                (paciente.nombre, paciente.edad, paciente.prevision, id_depto, paciente.rut)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar paciente: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(rut: str) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM paciente WHERE rut = ?", (rut.upper(),))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar paciente: {e}")
            return False
        finally:
            conn.close()