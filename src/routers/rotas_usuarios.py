from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_bd
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from src.schema.schemas import Usuario
from typing import List

router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_bd)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@router.get('/usuarios', response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_bd)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios