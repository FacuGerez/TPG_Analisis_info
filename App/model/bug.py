from pydantic import BaseModel

class Bug(BaseModel):
    id: int
    description: str
    tarea_id: int
    ticket_id: int