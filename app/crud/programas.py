import logging
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List


logger = logging.getLogger(__name__)


def update_url_pdf(db: Session, cod: int, url: str) -> bool:
    """Actualiza el campo `url_pdf` del programa indicado por `cod`."""
    try:
        query = text("""UPDATE programas_formacion SET url_pdf = :url_pdf WHERE cod_programa = :codigo""")
        db.execute(query, {"url_pdf": url, "codigo": cod})
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al actualizar url_pdf: {e}")
        raise Exception("Error de base de datos al actualizar url_pdf")
    
    
def get_programa_by_cod(db: Session, cod: int):
    """Obtiene un programa por su código"""
    try:
        query = text("""SELECT * FROM programas_formacion WHERE cod_programa = :codigo""")
        result = db.execute(query, {"codigo": cod}).mappings().first()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al consultar programa: {e}")
        raise Exception("Error al consultar programa")


def get_all_programas(db: Session):
    """Obtiene todos los programas de formación"""
    try:
        query = text("""
            SELECT cod_programa, version, nombre, nivel, 
                   tiempo_duracion, estado, url_pdf
            FROM programas_formacion
            ORDER BY nombre
        """)
        result = db.execute(query).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener programas: {e}")
        raise Exception("Error de base de datos al obtener los programas")


def get_programas_activos(db: Session):
    """Obtiene solo los programas activos"""
    try:
        query = text("""
            SELECT cod_programa, version, nombre, nivel, 
                   tiempo_duracion, estado, url_pdf
            FROM programas_formacion
            WHERE estado = 1
            ORDER BY nombre
        """)
        result = db.execute(query).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener programas activos: {e}")
        raise Exception("Error de base de datos al obtener los programas activos")