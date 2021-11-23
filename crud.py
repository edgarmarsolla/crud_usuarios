from typing import List
from sqlalchemy.orm import Session
from exceptions import Usuario_ja_existente, Usuario_nao_encontrado, Endereco_nao_encontrado, Endereco_ja_existente
from models import Usuario_informacaos, Endereco_informacaos
from schemas import Criando_atualizando_usuario, Criando_atualizando_endereco


# Função que lista as informação dos usuarios
def get_todos_usuarios(session: Session, limit: int, offset: int) -> List[Usuario_informacaos]:
    return session.query(Usuario_informacaos).offset(offset).limit(limit).all()


# Função que lista os endereços dos usuarios
def get_todos_enderecos(session: Session, limit: int, offset: int) -> List[Endereco_informacaos]:
    return session.query(Endereco_informacaos).offset(offset).limit(limit).all()


# Função que lista o usuario individual
def get_usuarios_por_id(session: Session, _id: int) -> Usuario_informacaos:
    usuario = session.query(Usuario_informacaos).get(_id)

    if usuario is None:
        raise Usuario_nao_encontrado

    return usuario


# Função que lista o endereço individual
def get_endereco_por_id(session: Session, _id: int) -> Endereco_informacaos:
    endereco = session.query(Endereco_informacaos).get(_id)

    if endereco is None:
        raise Endereco_nao_encontrado

    return endereco


# Função para adicionar um novo usuario no banco de dados
def criar_usuario(session: Session, usuario_informacao: Criando_atualizando_usuario) -> Usuario_informacaos:
    usuario_detales = session.query(Usuario_informacaos).filter(Usuario_informacaos.usuario_nome == usuario_informacao.usuario_nome, Usuario_informacaos.usuario_email == usuario_informacao.usuario_email, Usuario_informacaos.usuario_cpf == usuario_informacao.usuario_cpf, Usuario_informacaos.usuario_pis == usuario_informacao.usuario_pis, Usuario_informacaos.usuario_senha == usuario_informacao.usuario_senha).first()
    if usuario_detales is not None:
        raise Usuario_ja_existente

    novo_usuario = Usuario_informacaos(**usuario_informacao.dict())
    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)
    return novo_usuario


# Função para adicionar um novo endereço no banco de dados
def criar_endereco(session: Session, endereco: Criando_atualizando_endereco) -> Endereco_informacaos:
    endereco_informacao = session.query(Endereco_informacaos).filter(Endereco_informacaos.endereco_pais == endereco.endereco_pais, Endereco_informacaos.endereco_estado == endereco.endereco_estado, Endereco_informacaos.endereco_municipio == endereco.endereco_municipio, Endereco_informacaos.endereco_cep == endereco.endereco_cep, Endereco_informacaos.endereco_logradouro == endereco.endereco_logradouro, Endereco_informacaos.endereco_numero_da_casa == endereco.endereco_numero_da_casa, Endereco_informacaos.endereco_complemento == endereco.endereco_complemento, Endereco_informacaos.endereco_usuario == endereco.endereco_usuario).first()
    if endereco_informacao is not None:
        raise Endereco_ja_existente

    novo_endereco = Endereco_informacaos(**endereco.dict())
    session.add(novo_endereco)
    session.commit()
    session.refresh(novo_endereco)
    return novo_endereco


# Função para atualizar o usuario
def update_usuario_informacao(session: Session, _id: int, informacao_usuario_atualizada: Criando_atualizando_usuario) -> Usuario_informacaos:
    usuario_informacao = get_usuarios_por_id(session, _id)

    if usuario_informacao is None:
        raise Usuario_nao_encontrado

    usuario_informacao.usuario_nome = informacao_usuario_atualizada.usuario_nome
    usuario_informacao.usuario_email = informacao_usuario_atualizada.usuario_email
    usuario_informacao.usuario_cpf = informacao_usuario_atualizada.usuario_cpf
    usuario_informacao.usuario_pis = informacao_usuario_atualizada.usuario_pis
    usuario_informacao.usuario_senha = informacao_usuario_atualizada.usuario_senha

    session.commit()
    session.refresh(usuario_informacao)

    return usuario_informacao


# Função para atualizar o endereço
def update_endereco_informacao(session: Session, _id: int, informacao_edereco_atualizado: Criando_atualizando_endereco) -> Endereco_informacaos:
    endereco_informacao = get_endereco_por_id(session, _id)

    if endereco_informacao is None:
        raise Endereco_nao_encontrado

    endereco_informacao.endereco_pais = informacao_edereco_atualizado.endereco_pais
    endereco_informacao.endereco_estado = informacao_edereco_atualizado.endereco_estado
    endereco_informacao.endereco_municipio = informacao_edereco_atualizado.endereco_municipio
    endereco_informacao.endereco_cep = informacao_edereco_atualizado.endereco_cep
    endereco_informacao.endereco_logradouro = informacao_edereco_atualizado.endereco_logradouro
    endereco_informacao.endereco_complemento = informacao_edereco_atualizado.endereco_complemento

    session.commit()
    session.refresh(endereco_informacao)

    return endereco_informacao


# Função para deletar informações do usuario
def delete_informacao_usuario(session: Session, _id: int):
    usuario_informacao = get_usuarios_por_id(session, _id)

    if usuario_informacao is None:
        raise Usuario_nao_encontrado

    session.delete(usuario_informacao)
    session.commit()

    return


# Função para deletar o endereço do usuario
def delete_indormacao_endereco(session: Session, _id: int):
    endereco_informacao = get_endereco_por_id(session, _id)

    if endereco_informacao is None:
        raise Usuario_nao_encontrado

    session.delete(endereco_informacao)
    session.commit()

    return
