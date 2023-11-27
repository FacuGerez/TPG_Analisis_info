from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    severity: str
    priority: str
    description: str


class TicketCreate(TicketBase):
    #Para que el estado se inicialice en Abierto
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = "Abierto"

class Ticket(TicketBase):
    id: int
    client_id: int
    product_id: int

    class Config:
        orm_mode = True
