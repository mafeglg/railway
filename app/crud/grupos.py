
import logging
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List


logger = logging.getLogger(__name__)


def get_all_grupos(db: Session):
    """Obtiene todos los grupos con información del programa y centro"""
    try:
        query = text("""
            SELECT 
                g.ficha, 
                g.cod_programa, 
                g.cod_centro,
                g.modalidad,
                g.jornada,
                g.etapa_ficha,
                g.estado_curso,
                g.fecha_inicio,
                g.fecha_fin,
                g.nombre_responsable,
                p.nombre as nombre_programa,
                c.nombre_centro
            FROM grupos g
            LEFT JOIN programas_formacion p ON g.cod_programa = p.cod_programa
            LEFT JOIN centros_formacion c ON g.cod_centro = c.cod_centro
            ORDER BY g.ficha DESC
        """)
        result = db.execute(query).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener grupos: {e}")
        raise Exception("Error de base de datos al obtener los grupos")


def get_grupo_by_ficha(db: Session, ficha: int):
    """Obtiene un grupo por su número de ficha"""
    try:
        query = text("""
            SELECT 
                g.ficha, 
                g.cod_programa, 
                g.cod_centro,
                g.modalidad,
                g.jornada,
                g.etapa_ficha,
                g.estado_curso,
                g.fecha_inicio,
                g.fecha_fin,
                g.nombre_responsable,
                p.nombre as nombre_programa,
                c.nombre_centro
            FROM grupos g
            LEFT JOIN programas_formacion p ON g.cod_programa = p.cod_programa
            LEFT JOIN centros_formacion c ON g.cod_centro = c.cod_centro
            WHERE g.ficha = :ficha
        """)
        result = db.execute(query, {"ficha": ficha}).mappings().first()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener grupo por ficha: {e}")
        raise Exception("Error de base de datos al obtener el grupo")


def get_grupos_by_programa(db: Session, cod_programa: int):
    """Obtiene todos los grupos de un programa específico"""
    try:
        query = text("""
            SELECT 
                g.ficha, 
                g.cod_programa, 
                g.cod_centro,
                g.modalidad,
                g.jornada,
                g.etapa_ficha,
                g.estado_curso,
                g.fecha_inicio,
                g.fecha_fin,
                g.nombre_responsable,
                p.nombre as nombre_programa,
                c.nombre_centro
            FROM grupos g
            LEFT JOIN programas_formacion p ON g.cod_programa = p.cod_programa
            LEFT JOIN centros_formacion c ON g.cod_centro = c.cod_centro
            WHERE g.cod_programa = :cod_programa
            ORDER BY g.ficha DESC
        """)
        result = db.execute(query, {"cod_programa": cod_programa}).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener grupos por programa: {e}")
        raise Exception("Error de base de datos al obtener los grupos del programa")


def get_grupos_by_centro(db: Session, cod_centro: int):
    """Obtiene todos los grupos de un centro específico"""
    try:
        query = text("""
            SELECT 
                g.ficha, 
                g.cod_programa, 
                g.cod_centro,
                g.modalidad,
                g.jornada,
                g.etapa_ficha,
                g.estado_curso,
                g.fecha_inicio,
                g.fecha_fin,
                g.nombre_responsable,
                p.nombre as nombre_programa,
                c.nombre_centro
            FROM grupos g
            LEFT JOIN programas_formacion p ON g.cod_programa = p.cod_programa
            LEFT JOIN centros_formacion c ON g.cod_centro = c.cod_centro
            WHERE g.cod_centro = :cod_centro
            ORDER BY g.ficha DESC
        """)
        result = db.execute(query, {"cod_centro": cod_centro}).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener grupos por centro: {e}")
        raise Exception("Error de base de datos al obtener los grupos del centro")