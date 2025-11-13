from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from app.crud.programas import get_programa_by_cod, update_url_pdf
from utils.utils import save_uploaded_document
from core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/programas",
    tags=["Documentos"]
)

@router.post("/subir-pdf/")
def upload_document(
    codigo: int,
    file: UploadFile = File(...),
    db: Session= Depends(get_db)
):
    """
    Sube un archivo PDF, Word o Excel al servidor y devuelve su ruta de almacenamiento.
    """
    try:
        programa=get_programa_by_cod(db, codigo)
        
        if programa is None:
            raise HTTPException(status_code=404, detail="El programa no existe en base de datos")
        
        file_path = save_uploaded_document(file)
        # actualizar url en la base de datos: update_url_pdf(db, codigo, url)
        save_url = update_url_pdf(db, codigo, file_path)
        return {
            "message": "Archivo subido correctamente",
            "filename": file.filename,
            "ruta_servidor": file_path
        }
    except HTTPException as e:
        # Retorna los errores personalizados definidos en la función
        raise e
    except Exception as e:
        # Captura cualquier otro error inesperado
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
