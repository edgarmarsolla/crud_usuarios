from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from database import Base


class Usuario_informacaos(Base):
    __tablename__ = "usuario"
    usuario_id = Column(Integer, primary_key=True, index=True)
    usuario_nome = Column(String)
    usuario_email = Column(String)
    usuario_cpf = Column(String)
    usuario_pis = Column(String)
    usuario_senha = Column(String)
    usuario_edereco = relationship("Endereco_informacaos",)


class Endereco_informacaos(Base):
    __tablename__ = "endereco"
    endereco_id = Column(Integer, primary_key=True, index=True)
    endereco_pais = Column(String)
    endereco_estado = Column(String)
    endereco_municipio = Column(String)
    endereco_cep = Column(String)
    endereco_logradouro = Column(String)
    endereco_numero_da_casa = Column(String)
    endereco_complemento = Column(String)
    endereco_usuario = Column(Integer, ForeignKey('usuario.usuario_id'))



