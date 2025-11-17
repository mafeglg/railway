from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.router.dependencias import get_current_user
from core.database import get_db
from app.schemas.grupos import RetornoGrupo
from app.schemas.usuarios import RetornoUsuario
from app.crud import grupos as crud_grupos
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter(
    prefix="/grupos",
    tags=["Grupos de Formación"]
)


@router.get("/obtener-todos", status_code=status.HTTP_200_OK, response_model=List[RetornoGrupo])
def get_all(
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Obtiene todos los grupos de formación
    """
    try:
        grupos = crud_grupos.get_all_grupos(db)
        if not grupos:
            raise HTTPException(status_code=404, detail="No se encontraron grupos")
        return grupos
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/obtener-por-ficha/{ficha}", status_code=status.HTTP_200_OK, response_model=RetornoGrupo)
def get_by_ficha(
    ficha: int,
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Obtiene un grupo por su número de ficha
    """
    try:
        grupo = crud_grupos.get_grupo_by_ficha(db, ficha)
        if not grupo:
            raise HTTPException(status_code=404, detail="Grupo no encontrado")
        return grupo
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/obtener-por-programa/{cod_programa}", status_code=status.HTTP_200_OK, response_model=List[RetornoGrupo])
def get_by_programa(
    cod_programa: int,
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Obtiene todos los grupos de un programa específico
    """
    try:
        grupos = crud_grupos.get_grupos_by_programa(db, cod_programa)
        if not grupos:
            raise HTTPException(status_code=404, detail="No se encontraron grupos para este programa")
        return grupos
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/obtener-por-centro/{cod_centro}", status_code=status.HTTP_200_OK, response_model=List[RetornoGrupo])
def get_by_centro(
    cod_centro: int,
    db: Session = Depends(get_db),
    user_token: RetornoUsuario = Depends(get_current_user)
):
    """
    Obtiene todos los grupos de un centro específico
    """
    try:
        grupos = crud_grupos.get_grupos_by_centro(db, cod_centro)
        if not grupos:
            raise HTTPException(status_code=404, detail="No se encontraron grupos para este centro")
        return grupos
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))