from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    nome: str
    id: Optional[str] = None
    telefone: str
    #meus_produtos = List['Produto']
    #minhas_vendas = List['Pedido']
    #minhas_compras = List['Pedido']

    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    nome: str
    preco: float

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
