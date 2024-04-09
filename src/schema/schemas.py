from pydantic import BaseModel
from typing import Optional, List

class ProdutoSimplesListar(BaseModel):
    id: Optional[int]
    nome: str
    preco: float

    class Config:
        from_attributes = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimplesListar] = []
    #minhas_vendas = List['Pedido']
    #minhas_compras = List['Pedido']
    #produtos: List[produtos] = []

    class Config:
        from_attributes = True

class UsuarioSimples(BaseModel):
    nome: str
    telefone: str
    id: Optional[int] = None

    class Config:
        from_attributes = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]

    class Config:
        from_attributes = True

class ProdutoSimples(BaseModel):
    nome: str
    preco: float
    usuario: Usuario

    class Config:
        from_attributes = True

class ProdutoSimplesAtualizar(BaseModel):
    nome: str
    preco: float

    class Config:
        from_attributes = True

class Pedido(BaseModel):
    id: Optional[int] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
