from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.produto import RepositorioProduto
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from src.schema.schemas import Produto, Usuario, ProdutoSimples, UsuarioSimples, ProdutoSimplesAtualizar
from src.infra.sqlalchemy.config.database import get_bd

router = APIRouter()

@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_bd)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_bd)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.put('/produtos/{id}', response_model=ProdutoSimplesAtualizar)
def atualizar_produto(id: int, produto: ProdutoSimplesAtualizar, db: Session = Depends(get_bd)):
    RepositorioProduto(db).editar(id, produto)
    return produto

@router.delete('/produtos/{id}')
def deletar_produto(id: int, db: Session = Depends(get_bd)):
    RepositorioProduto(db).remover(id)
    return {"mensagem": "produto removido"}
