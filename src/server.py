from fastapi import FastAPI, Depends, status
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from src.schema.schemas import Usuario
from src.infra.sqlalchemy.config.database import get_bd
from src.routers import rotas_produtos

origins = ['http://127.0.0.1:8000/']

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]


app = FastAPI()


#PRODUTOS
app.include_router(rotas_produtos.router)


#USUARIOS

@app.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_bd)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_bd)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios