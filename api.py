from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_todos_usuarios, get_todos_enderecos, get_usuarios_por_id, get_endereco_por_id, criar_usuario, criar_endereco, update_usuario_informacao, update_endereco_informacao, delete_informacao_usuario, delete_indormacao_endereco
from database import get_db
from exceptions import Usuario_informacao_exception, Endereco_informacao_exception
from schemas import Usuario, Endereco, Criando_atualizando_usuario, Criando_atualizando_endereco, Usuario_informacao, Endereco_informacao

router = APIRouter()


@cbv(router)
class Usuarios:
    session: Session = Depends(get_db)

    # Para obter a lista de informaçãos do usuarios
    @router.get("/usuarios", response_model=Usuario_informacao)
    def lista_de_usuarios(self, limit: int = 10, offset: int = 0):
        usuario_lista = get_todos_usuarios(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": usuario_lista}

        return response

    # Para obter a lista de endereços do usuarios
    @router.get("/endereco", response_model=Endereco_informacao)
    def lista_de_endereco(self, limit: int = 10, offset: int = 0):
        endereco_lista = get_todos_enderecos(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": endereco_lista}

        return response

    # Endpoint para adicionar informações do usuario no banco de dados
    @router.post("/addusuarios")
    def add_usuario(self, usuario_informacao: Criando_atualizando_usuario):

        try:
            usuario_informacao = criar_usuario(self.session, usuario_informacao)
            return usuario_informacao
        except Usuario_informacao_exception as cie:
            raise HTTPException(**cie.__dict__)

    # Endpoint para adicionar informações de endereço do usuario no banco de dados
    @router.post("/addendereco")
    def add_endereco(self, endereco_informacao: Criando_atualizando_endereco):

        try:
            endereco_informacao = criar_endereco(self.session, endereco_informacao)
            return endereco_informacao
        except Endereco_informacao_exception as cie:
            raise HTTPException(**cie.__dict__)


# Endpoint para leitura das informação particular do usuario
@router.get("/usuario/{usuario_id}", response_model=Usuario)
def get_usuario_info(usuario_id: int, session: Session = Depends(get_db)):

    try:
        usuario_info = get_usuarios_por_id(session, usuario_id)
        return usuario_info
    except Usuario_informacao_exception as cie:
        raise HTTPException(**cie.__dict__)


# Endpoint para leitura do endereço particular do usuario
@router.get("/endereco/{endereco_id}", response_model=Endereco)
def get_endereco_info(endereco_id: int, session: Session = Depends(get_db)):

    try:
        endereco_info = get_endereco_por_id(session, endereco_id)
        return endereco_info
    except Endereco_informacao_exception as cie:
        raise HTTPException(**cie.__dict__)


# Atualizando Usuario ja existente
@router.put("/usuarioput/{usuario_id}", response_model=Usuario)
def update_usuario(usuario_id: int, new_info: Criando_atualizando_usuario, session: Session = Depends(get_db)):

    try:
        usuario_info = update_usuario_informacao(session, usuario_id, new_info)
        return usuario_info
    except Usuario_informacao_exception as cie:
        raise HTTPException(**cie.__dict__)


# Atualizando Endereco ja existente
@router.put("/enderecoput/{endereco_id}", response_model=Endereco)
def update_endereco(endereco_id: int, new_info: Criando_atualizando_endereco, session: Session = Depends(get_db)):

    try:
        endereco_info = update_endereco_informacao(session, endereco_id, new_info)
        return endereco_info
    except Endereco_informacao_exception as cie:
        raise HTTPException(**cie.__dict__)


# Deleta informações do usuario
@router.delete("/usuariodel/{usuario_id}")
def delete_usuario(usuario_id: int, session: Session = Depends(get_db)):

    try:
        return delete_informacao_usuario(session, usuario_id)
    except Usuario_informacao_exception as cie:
        raise HTTPException(**cie.__dict__)


# Deleta Endereõ do usuario
@router.delete("/enderecodel/{endereco_id}")
def delete_endereco(endereco_id: int, session: Session = Depends(get_db)):

    try:
        return delete_indormacao_endereco(session, endereco_id)
    except Endereco_informacao_exception as cie:
        raise HTTPException(**cie.__dict__)
