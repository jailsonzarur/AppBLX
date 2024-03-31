from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    #meus_produtos = List['Produto']
    #minhas_vendas = List['Pedido']
    #minhas_compras = List['Pedido']
    #produtos: List[produtos] = []

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    nome: str
    telefone: str
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    nome: str
    preco: float

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[int] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
