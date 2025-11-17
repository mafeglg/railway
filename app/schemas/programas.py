from typing import Optional
from pydantic import BaseModel, Field


class ProgramaBase(BaseModel):
    cod_programa: int
    version: str
    nombre: str
    nivel: str
    tiempo_duracion: int
    estado: bool
    url_pdf: Optional[str] = None

class RetornoPrograma(ProgramaBase):
    pass

class ActualizarPrograma(BaseModel):
    version: Optional[str] = None
    nombre: Optional[str] = Field(default=None, max_length=200)
    nivel: Optional[str] = None
    tiempo_duracion: Optional[int] = None
    estado: Optional[bool] = None
    url_pdf: Optional[str] = None