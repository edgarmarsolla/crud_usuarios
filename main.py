from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)

origins = [
    "https://projetocrudusuario.herokuapp.com/",
    "https://projetocrudusuario.herokuapp.com/usuarios",
    "https://projetocrudusuario.herokuapp.com/endereco",
    "https://projetocrudusuario.herokuapp.com/addusuarios",
    "https://projetocrudusuario.herokuapp.com/addendereco",
    "https://projetocrudusuario.herokuapp.com/usuario/{usuario_id}",
    "https://projetocrudusuario.herokuapp.com/endereco/{endereco_id}",
    "https://projetocrudusuario.herokuapp.com/usuarioput/{usuario_id}",
    "https://projetocrudusuario.herokuapp.com/enderecoput/{endereco_id}",
    "https://projetocrudusuario.herokuapp.com/enderecodel/{usuario_id}",
    "https://projetocrudusuario.herokuapp.com/enderecodel/{endereco_id}"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"menssagem": "Hellow Word"}