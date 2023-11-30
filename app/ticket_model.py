from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    severity: str
    priority: str
    description: str


class TicketCreate(TicketBase):
    pass


class TicketUpdate(TicketBase):
    state: str


class Ticket(TicketBase):
    id: int
    client_id: int
    version_id: int
    state: str
    date_creacion: str

    class Config:
        orm_mode = True
