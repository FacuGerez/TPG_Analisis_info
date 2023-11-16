from pydantic import BaseModel
from ticket import Ticket


class ClientBase(BaseModel):
    name: str
    # .....a completar


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int
    tickets: list[Ticket] = []

    class Config:
        orm_mode = True
