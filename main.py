from typing import Optional
from pydantic import BaseModel

class Formulario(BaseModel):
    nombre: str
    apellido: str
    correo_electronico: str
    descripcion: Optional[str]
    curso: str
    ano: int
    direccion: str
    codigo_postal: Optional[int]
    password: str

