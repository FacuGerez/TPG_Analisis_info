from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    severity: str
    priority: str


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    client_id: int
    product_id: int
    state: str

    class Config:
        orm_mode = True
