from pydantic import BaseModel

class Ticket(BaseModel):
    nroTicket: int
    Title: str
    Description: str
    Severity: str
    Priority: str
    State: str