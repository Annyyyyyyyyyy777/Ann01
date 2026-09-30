class Paciente:

    PREVISIONES: set[str] = {"Fonasa", "Isapre"}

    def __init__(self, rut: str, nombre: str, edad: int, prevision:str):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision

    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self, rut: str)-> None:
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El RUT no puede estar vacío.")
        self._rut = rut.strip().upper()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = nombre.strip().upper()

    @property
    def edad(self)->int:
        return self._edad

    @edad.setter
    def edad(self, edad:int)->None:
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        if edad < 0 or edad > 125:
            raise ValueError("La edad debe ser un valor biológicamente válido (entre 0 y 125 años).")
        self._edad = edad

    @property
    def prevision(self)->str:
        return self._prevision

    @prevision.setter
    def prevision(self, prevision:str)->None:
        if not isinstance(prevision, str):
            raise TypeError("La previsión debe ser una cadena de texto.")
        prevision_limpio = prevision.strip().capitalize()
        if prevision_limpio not in self.PREVISIONES:
            opciones = ", ".join(self.PREVISIONES)
            raise ValueError(f"Previsión '{prevision}' no válida. Opciones permitidas: {opciones}.")
        self._prevision = prevision_limpio

    def __str__(self)->str:
        return f"Información del Paciente:\nRUT: {self.rut}\nNombre: {self.nombre}\nEdad: {self.edad}\nPrevisión: {self.prevision}"

    def __repr__(self)->str:
        return f"Paciente(rut='{self.rut}', nombre='{self.nombre}', edad={self.edad},prevision='{self.prevision}')"
    