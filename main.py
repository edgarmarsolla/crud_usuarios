from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)

origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/usuarios",
    "http://127.0.0.1:8000/endereco",
    "http://127.0.0.1:8000/addusuarios",
    "http://127.0.0.1:8000/addendereco",
    "http://127.0.0.1:8000/usuario/{usuario_id}",
    "http://127.0.0.1:8000/endereco/{endereco_id}",
    "http://127.0.0.1:8000/usuarioput/{usuario_id}",
    "http://127.0.0.1:8000/enderecoput/{endereco_id}",
    "http://127.0.0.1:8000/enderecodel/{usuario_id}",
    "http://127.0.0.1:8000/enderecodel/{endereco_id}"

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