from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    severity: str
    priority: str


class TicketCreate(TicketBase):
    state: str


class Ticket(TicketBase):
    id: int
    client_id: int
    product_id: int

    class Config:
        orm_mode = True
