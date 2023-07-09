

from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Sexo(str, Enum):
    masculino = "masculino"
    feminino = "feminino"


class Pessoa(BaseModel):
    id: Optional[UUID] = uuid4()
    nome: str
    idade: int
    sexo: Sexo
