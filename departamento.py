class departamento:
    
    def __init__(self,id_depto:str,nombre:str,piso:int):

           self.id_depto = id_depto
           self.nombre = nombre
           self.piso = piso

    @property
    def id_depto(self)->str:
        return self._id_depto

    @id_depto.setter
    def id_depto(self,id_depto:str)->None:
        self._id_depto

    @property
    def nombre(self) -> None:
        return self._nombre 

    @nombre.setter
    def nombre(self,nombre:str)->None:
        self._nombre = nombre 

    @property
    def piso(self)->str:
        return self._piso

    @piso.setter
    def piso(self,piso:str)->None:
        self._piso = piso

    def __str__(self)->str:
        return f"Informacion del departamento:\nID_DEPARTAMENTO:{self.id_departamento}\nNombre:{self.nombre}\nPiso:{self.piso}"
    def __repr__(self)->str:
        return