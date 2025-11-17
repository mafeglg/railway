from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class GrupoBase(BaseModel):
    ficha: int
    cod_programa: int
    cod_centro: int
    modalidad: Optional[str] = None
    jornada: Optional[str] = None
    etapa_ficha: Optional[str] = None
    estado_curso: Optional[str] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    nombre_responsable: Optional[str] = None

class RetornoGrupo(GrupoBase):
    nombre_programa: Optional[str] = None
    nombre_centro: Optional[str] = None

class ActualizarGrupo(BaseModel):
    modalidad: Optional[str] = None
    jornada: Optional[str] = None
    etapa_ficha: Optional[str] = None
    estado_curso: Optional[str] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    nombre_responsable: Optional[str] = None