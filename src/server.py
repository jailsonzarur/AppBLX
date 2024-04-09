from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.produto import RepositorioProduto
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from src.schema.schemas import Produto, Usuario, ProdutoSimples, UsuarioSimples, ProdutoSimplesAtualizar
from src.infra.sqlalchemy.config.database import get_bd, criar_bd

criar_bd()

app = FastAPI()

#CORS
app.middleware(CORSMiddleware,
               allow_origins = ['http://localhost:3000'],
               allow_credentials = True,
               allow_methods=["*"],
               allow_headers=["*"])


#PRODUTOS

@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_bd)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_bd)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.put('/produtos/{id}', response_model=ProdutoSimplesAtualizar)
def atualizar_produto(id: int, produto: ProdutoSimplesAtualizar, db: Session = Depends(get_bd)):
    RepositorioProduto(db).editar(id, produto)
    return produto

@app.delete('/produtos/{id}')
def deletar_produto(id: int, db: Session = Depends(get_bd)):
    RepositorioProduto(db).remover(id)
    return {"mensagem": "produto removido"}

#USUARIOS

@app.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_bd)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_bd)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios