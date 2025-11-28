from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class GrupoBase(BaseModel):
    cod_programa: Optional[int] = None
    cod_centro: Optional[int] = None
    modalidad: Optional[str] = Field(default=None, max_length=80)
    jornada: Optional[str] = Field(default=None, max_length=80)
    etapa_ficha: Optional[str] = Field(default=None, max_length=80)
    estado_curso: Optional[str] = Field(default=None, max_length=80)
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    cod_municipio: Optional[str] = Field(default=None, min_length=1, max_length=5)
    cod_estrategia: Optional[str] = Field(default=None, min_length=1, max_length=5)
    nombre_responsable: Optional[str] = Field(default=None, max_length=150)
    cupo_asignado: Optional[int] = None
    num_aprendices_fem: Optional[int] = None
    num_aprendices_mas: Optional[int] = None
    num_aprendices_nobin: Optional[int] = None
    num_aprendices_matriculados: Optional[int] = None
    num_aprendices_activos: Optional[int] = None
    tipo_doc_empresa: Optional[str] = Field(default=None, max_length=5)
    num_doc_empresa: Optional[str] = Field(default=None, max_length=30)
    nombre_empresa: Optional[str] = Field(default=None, max_length=140)


class CrearGrupo(GrupoBase):
    ficha: int


class RetornoGrupo(GrupoBase):
    ficha: int


class ActualizarGrupo(BaseModel):
    cod_programa: Optional[int] = None
    cod_centro: Optional[int] = None
    modalidad: Optional[str] = Field(default=None, max_length=80)
    jornada: Optional[str] = Field(default=None, max_length=80)
    etapa_ficha: Optional[str] = Field(default=None, max_length=80)
    estado_curso: Optional[str] = Field(default=None, max_length=80)
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    cod_municipio: Optional[str] = Field(default=None, min_length=1, max_length=5)
    cod_estrategia: Optional[str] = Field(default=None, min_length=1, max_length=5)
    nombre_responsable: Optional[str] = Field(default=None, max_length=150)
    cupo_asignado: Optional[int] = None
    num_aprendices_fem: Optional[int] = None
    num_aprendices_mas: Optional[int] = None
    num_aprendices_nobin: Optional[int] = None
    num_aprendices_matriculados: Optional[int] = None
    num_aprendices_activos: Optional[int] = None
    tipo_doc_empresa: Optional[str] = Field(default=None, max_length=5)
    num_doc_empresa: Optional[str] = Field(default=None, max_length=30)
    nombre_empresa: Optional[str] = Field(default=None, max_length=140)