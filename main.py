
from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Pessoa

app = FastAPI()
# criando um DB local
db: List[Pessoa] = [
    Pessoa(id=uuid4(), nome="tarcisio do acordeon", idade=48, sexo="masculino"),
    Pessoa(id=uuid4(), nome="Wesley safadão", idade=50, sexo="masculino"),
    Pessoa(id=uuid4(), nome="Julia", idade=48, sexo="masculino"),
    Pessoa(id=uuid4(), nome="Cinara", idade=48, sexo="feminino"),
    Pessoa(id=uuid4(), nome="curt cobain", idade=48, sexo="masculino")
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ListaPessoas")
async def get_users():
    return db
