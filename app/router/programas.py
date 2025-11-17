from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from app.crud.programas import (
    get_programa_by_cod, 
    update_url_pdf, 
    get_all_programas,
    get_programas_activos
)

from app.schemas.programas import RetornoPrograma
from app.schemas.usuarios import RetornoUsuario
from app.router.dependencias import get_current_user
from utils.utils import save_uploaded_document
from core.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter(
    prefix="/programas",
    tags=["Programas de Formación"]
)

@router.post("/subir-pdf/")
def upload_document(
    codigo: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Sube un archivo PDF del programa de formación
    """
    try:
        programa = get_programa_by_cod(db, codigo)
        
        if programa is None:
            raise HTTPException(status_code=404, detail="El programa no existe en base de datos")
        
        file_path = save_uploaded_document(file)
        save_url = update_url_pdf(db, codigo, file_path)
        
        return {
            "message": "Archivo subido correctamente",
            "filename": file.filename,
            "ruta_servidor": file_path
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


@router.get("/obtener-todos", status_code=status.HTTP_200_OK, response_model=List[RetornoPrograma])
def get_all(
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Obtiene todos los programas de formación
    """
    try:
        programas = get_all_programas(db)
        if not programas:
            raise HTTPException(status_code=404, detail="No se encontraron programas")
        return programas
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/obtener-activos", status_code=status.HTTP_200_OK, response_model=List[RetornoPrograma])
def get_activos(
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Obtiene solo los programas activos
    """
    try:
        programas = get_programas_activos(db)
        if not programas:
            raise HTTPException(status_code=404, detail="No se encontraron programas activos")
        return programas
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/obtener-por-codigo/{codigo}", status_code=status.HTTP_200_OK, response_model=RetornoPrograma)
def get_by_codigo(
    codigo: int,
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Obtiene un programa por su código
    """
    try:
        programa = get_programa_by_cod(db, codigo)
        if not programa:
            raise HTTPException(status_code=404, detail="Programa no encontrado")
        return programa
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))