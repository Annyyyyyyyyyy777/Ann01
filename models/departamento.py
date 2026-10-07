class Departamento:
    """
    Modelo (DTO) para la entidad Departamento.
    Atributos:
    - id_departamento (int | None): Identificador único del departamento en BD.
    - nombre (str): Nombre del departamento (e.g. Pediatría, Urgencias).
    - piso (int): Piso donde se ubica el departamento.
    """

    def __init__(self, nombre: str, piso: int, id_departamento: int | None = None):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.piso = piso

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre del departamento debe tener al menos 3 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def piso(self) -> int:
        return self._piso

    @piso.setter
    def piso(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("El piso debe ser un número entero.")
        self._piso = valor

    def __str__(self) -> str:
        id_str = self.id_departamento if self.id_departamento is not None else 'Sin asignar'
        return f"Departamento [ID: {id_str}] | Nombre: {self.nombre} | Piso: {self.piso}"

    def __repr__(self) -> str:
        return f"Departamento(id_departamento={self.id_departamento}, nombre='{self.nombre}', piso={self.piso})"