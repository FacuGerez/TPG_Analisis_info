from pydantic import BaseModel

class Ticket(BaseModel):
    id: int
    title: str
    severity: str
    priority: str
    state: str
    client_id: int