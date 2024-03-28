from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from infra.sqlalchemy.repositories.produto import RepositorioProduto
from infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from schema.schemas import Produto, Usuario, ProdutoSimples
from infra.sqlalchemy.config.database import get_bd, criar_bd

criar_bd()

app = FastAPI()

@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_bd)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_bd)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/usuarios')
def criar_usuario(usuario: Usuario, db: Session = Depends(get_bd)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios')
def listar_usuarios(db: Session = Depends(get_bd)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios