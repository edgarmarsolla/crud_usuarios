from pydantic import BaseModel
from typing import Optional, List


# Apoia a criação e atualização de API
class Criando_atualizando_usuario(BaseModel):
    usuario_nome: str
    usuario_email: str
    usuario_cpf: str
    usuario_pis: str
    usuario_senha: str


# Ajuda na listagem da API
class Usuario(Criando_atualizando_usuario):
    usuario_id: int

    class Config:
        orm_mode = True


# Ajuda na listagem de Usuarios na API dando um limit
class Usuario_informacao(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]


# Apoia a criação e atualização de API
class Criando_atualizando_endereco(BaseModel):
    endereco_pais: str
    endereco_estado: str
    endereco_municipio: str
    endereco_cep: str
    endereco_logradouro: str
    endereco_numero_da_casa: str
    endereco_complemento: str
    endereco_usuario: int


# Ajuda na listagem da API
class Endereco(Criando_atualizando_endereco):
    endereco_id: int

    class Config:
        orm_mode = True


# Ajuda na listagem de Endereco na API dando um limit
class Endereco_informacao(BaseModel):
    limit: int
    offset: int
    data: List[Endereco]

