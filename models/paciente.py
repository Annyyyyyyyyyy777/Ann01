from models.departamento import Departamento

class Paciente:
    """
    Modelo (DTO) para la entidad Paciente.
    """
    PREVISIONES: set[str] = {"Fonasa", "Isapre", "Particular", "Otro"}

    def __init__(self, rut: str, nombre: str, edad: int, prevision: str, departamento: Departamento | None = None):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision
        self.departamento = departamento

    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self, rut: str) -> None:
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El RUT no puede estar vacío.")
        self._rut = rut.strip().upper()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = nombre.strip().title()
 
    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, edad: int) -> None:
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        if edad < 0 or edad > 125:
            raise ValueError("La edad debe ser un valor biológicamente válido (entre 0 y 125 años).")
        self._edad = edad

    @property
    def prevision(self) -> str:
        return self._prevision

    @prevision.setter
    def prevision(self, prevision: str) -> None:
        if not isinstance(prevision, str):
            raise TypeError("La previsión debe ser una cadena de texto.")
        prevision_limpio = prevision.strip().capitalize()
        if prevision_limpio not in self.PREVISIONES:
            opciones = ", ".join(self.PREVISIONES)
            raise ValueError(f"Previsión '{prevision}' no válida. Opciones permitidas: {opciones}.")
        self._prevision = prevision_limpio

    @property
    def departamento(self) -> Departamento | None:
        return self._departamento

    @departamento.setter
    def departamento(self, departamento: Departamento | None) -> None:
        if departamento is not None and not isinstance(departamento, Departamento):
            raise TypeError("El departamento debe ser una instancia de la clase Departamento o None.")
        self._departamento = departamento

    def __str__(self) -> str:
        depto_str = self.departamento.nombre if self.departamento else "Ninguno"
        return f"""Paciente | RUT: {self.rut} | Nombre: {self.nombre} | Edad: {self.edad} 
        | Previsión: {self.prevision} | Departamento: {depto_str}"""

    def __repr__(self) -> str:
        return f"""Paciente(rut='{self.rut}', nombre='{self.nombre}', edad={self.edad}, 
        prevision='{self.prevision}', departamento={repr(self.departamento)})"""