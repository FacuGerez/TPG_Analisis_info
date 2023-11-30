from pydantic import BaseModel
from datetime import datetime


class TicketBase(BaseModel):
    title: str
    severity: str
    priority: str
    description: str


class TicketCreate(TicketBase):
    # Para que el estado se inicialice en Abierto
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state: str = "Abierto"
        self.date_creacion: str = datetime.now().strftime("Fecha : %d / %m / %Y , Horario : %H:%M:%S")


class Ticket(TicketBase):
    id: int
    client_id: int
    product_id: int

    class Config:
        orm_mode = True
