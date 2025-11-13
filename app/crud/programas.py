import logging
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


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
    
    try:
        query = text(f"""SELECT * FROM programas_formacion WHERE cod_programa = :codigo""")
        result= db.execute(query, {"codigo": cod}).mappings().first()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al consultar programa: {e}")
        raise Exception("Error al consultar programa")