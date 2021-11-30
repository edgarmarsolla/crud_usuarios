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
    " http://127.0.0.1:8000/usuarios"

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